// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// The Performance Checks page: each benchmark's headline trend, the suites' latest
// runs, and one benchmark's history per device, from the data.json
// ci/scripts/build_pages.py writes beside it.

(() => {
  const trendsHost = document.getElementById("iron-trends");
  const live = document.getElementById("iron-live");
  const runsHost = document.getElementById("iron-runs");
  const bench = document.getElementById("iron-bench");
  if (!trendsHost || !live || !runsHost || !bench) return;

  // The data-viz reference palette, in its validated order: light and dark
  // steps of the same eight hues. A ninth series is never drawn at once.
  const PALETTE = {
    light: ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"],
    dark: ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"],
  };
  const CRITICAL = "#d03b3b";
  // A trend's line style names its form where a card draws two.
  const DASHES = {
    "device loop": { dash: [], css: "solid" },
    "host loop": { dash: [7, 4], css: "dashed" },
    "each step": { dash: [2, 3], css: "dotted" },
  };
  const SUITE_ORDER = ["small", "examples", "extensive", "nightly"];

  const pick = { name: document.getElementById("iron-bench-name"),
                 suite: document.getElementById("iron-bench-suite"),
                 metric: document.getElementById("iron-bench-metric") };
  const about = document.getElementById("iron-bench-about");
  const chartsHost = document.getElementById("iron-bench-charts");
  const tableHost = document.getElementById("iron-bench-table");

  let DATA = null;
  let charts = [];
  let trendCharts = [];
  // The series drawn, each holding its palette slot while it stays drawn.
  let slots = new Map();
  let shown = "";

  function el(tag, props = {}, ...children) {
    const node = document.createElement(tag);
    for (const [key, value] of Object.entries(props)) {
      if (key === "class") node.className = value;
      else if (key in node) node[key] = value;
      else node.setAttribute(key, value);
    }
    for (const child of children) {
      if (child != null) node.append(child);
    }
    return node;
  }

  const parseDate = (text) => new Date(text.replace(" ", "T") + "Z");
  const dayFmt = new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", timeZone: "UTC" });
  const longDay = new Intl.DateTimeFormat("en-US", { year: "numeric", month: "short", day: "numeric", timeZone: "UTC" });
  const relative = new Intl.RelativeTimeFormat("en-US", { numeric: "auto" });
  const compact = new Intl.NumberFormat("en-US", { notation: "compact", maximumSignificantDigits: 3 });
  const brief = new Intl.NumberFormat("en-US", { maximumSignificantDigits: 3 });
  // A latency past a millisecond reads in the largest unit it fills.
  const SCALES = { "µs": [[1e6, "s"], [1e3, "ms"]] };

  function stamp(text) {
    return text.slice(0, 16) + " UTC";
  }

  function age(text) {
    const hours = (parseDate(text) - Date.now()) / 3.6e6;
    return Math.abs(hours) < 48 ? relative.format(Math.round(hours), "hour")
                                : relative.format(Math.round(hours / 24), "day");
  }

  function number(value) {
    return value.toLocaleString("en-US", Math.abs(value) >= 1000
      ? { maximumFractionDigits: 0 } : { maximumSignificantDigits: 5 });
  }

  function unitOf(metric) {
    return (DATA.metrics[metric] || {}).unit || "";
  }

  function withUnit(value, metric) {
    const unit = unitOf(metric);
    return unit ? `${number(value)} ${unit}` : number(value);
  }

  function direction(metric) {
    const higher = (DATA.metrics[metric] || {}).higher_is_better;
    return higher == null ? "" : higher ? "higher is better" : "lower is better";
  }

  function commitLink(sha) {
    return el("a", { href: `${DATA.repository}/commit/${sha}`, textContent: sha.slice(0, 7) });
  }

  function suiteName(suite) {
    const info = DATA.suites[suite];
    return info ? `${info.name} (${info.group.toLowerCase()})` : suite;
  }

  function verdictMark(verdict) {
    if (verdict === "better") return el("span", { class: "iron-mark iron-better", textContent: "▲ better" });
    if (verdict === "worse") return el("span", { class: "iron-mark iron-worse", textContent: "▼ worse" });
    return null;
  }

  function hashState() {
    const text = decodeURIComponent(location.hash.slice(1));
    if (!text.includes("=")) return { bench: text };
    return Object.fromEntries(new URLSearchParams(location.hash.slice(1)));
  }

  function link(name, suite, metric) {
    return "#" + new URLSearchParams({ bench: name, suite, metric }).toString();
  }

  function key(colour, form) {
    const mark = el("span", { class: "iron-key", "aria-hidden": "true" });
    if (form) {
      mark.classList.add("iron-key-form");
      mark.style.borderTopStyle = DASHES[form].css;
      mark.style.borderTopColor = colour;
    } else {
      mark.style.background = colour;
    }
    return mark;
  }

  function seriesOf(name, suite, label) {
    return DATA.benchmarks[name].suites[suite].series.find((s) => s.label === label);
  }

  // ── Trends ───────────────────────────────────────────────────────────────

  // A link to the history already shown changes no hash, so scroll to it here.
  function openHistory(hash) {
    if (location.hash === hash) bench.scrollIntoView({ behavior: "smooth" });
    else location.hash = hash;
  }

  // Each run's point on every line, so the tooltip reads both devices at a
  // date even though their runs start minutes apart.
  const RUN_SPAN = 12 * 3.6e6;
  function eachRun(chart, event) {
    const at = chart.scales.x.getValueForPixel(event.x);
    const found = chart.data.datasets.map((dataset, datasetIndex) => {
      let best = null;
      dataset.data.forEach((d, index) => {
        const gap = Math.abs(d.x - at);
        if (!best || gap < best.gap) best = { gap, datasetIndex, index };
      });
      return best;
    }).filter(Boolean);
    if (!found.length) return [];
    const nearest = found.reduce((a, b) => (a.gap <= b.gap ? a : b));
    const runTime = chart.data.datasets[nearest.datasetIndex].data[nearest.index].x;
    return found.filter(({ datasetIndex, index }) =>
      Math.abs(chart.data.datasets[datasetIndex].data[index].x - runTime) < RUN_SPAN)
      .map(({ datasetIndex, index }) =>
        ({ element: chart.getDatasetMeta(datasetIndex).data[index], datasetIndex, index }));
  }

  function trendCard(trend, devices, colours, domain, pending) {
    const { benchmark: name, title, suite, metric, caption, also, series } = trend;
    const href = link(name, suite, metric);
    const latest = series.map(({ device, label }) => {
      const points = seriesOf(name, suite, label).devices[device].points.filter((p) => metric in p[3]);
      return points[points.length - 1][3][metric];
    });
    const [scale, unit] = (SCALES[unitOf(metric)] || []).find(([factor]) => Math.max(...latest) >= factor)
      || [1, unitOf(metric)];
    const sense = direction(metric);
    const surface = css("--md-default-bg-color");
    const shapes = Object.fromEntries(series.map(({ label }) => {
      const test = seriesOf(name, suite, label).test;
      const params = test.slice(test.indexOf("[") + 1, -1);
      return [label, params.startsWith(`${name}-`) ? params.slice(name.length + 1) : params];
    }));
    const oneShape = new Set(Object.values(shapes)).size === 1 ? Object.values(shapes)[0] : null;
    const rows = [];
    const datasets = [];
    devices.forEach((device, slot) => {
      const lines = series.filter((line) => line.device === device);
      if (!lines.length) {
        rows.push(el("li", { class: "iron-muted" }, el("span", { class: "iron-trend-device" },
          el("span", { class: "iron-key iron-key-none", "aria-hidden": "true" }), DATA.devices[device]),
          el("span", { class: "iron-trend-value", textContent: "not run" })));
        return;
      }
      lines.forEach(({ label, form, context }) => {
        const s = seriesOf(name, suite, label);
        const run = s.devices[device];
        const points = run.points.filter((p) => metric in p[3]);
        const last = points[points.length - 1];
        const moved = run.changes[metric];
        const what = trend.group === "Models"
          ? [also && also in last[3] ? `${also} ${brief.format(last[3][also])} ${unitOf(also)}` : null,
             context].filter(Boolean).join(" · ") || null
          : oneShape ? null : shapes[label];
        rows.push(el("li", {},
          el("span", { class: "iron-trend-device" }, key(colours[slot], form), DATA.devices[device],
            form ? el("small", { class: "iron-trend-form", textContent: ` ${form}` }) : null),
          el("span", { class: "iron-trend-value" },
            el("strong", { textContent: brief.format(last[3][metric] / scale) }), unit ? ` ${unit}` : "",
            last[2] === false ? el("span", { class: "iron-mark iron-worse", textContent: " ✕", title: "Its checks failed" }) : null,
            moved ? verdictMark(moved[1]) : null),
          what ? el("small", { class: "iron-trend-what", textContent: what, title: what }) : null));
        datasets.push({
          label: form ? `${DATA.devices[device]}, ${form}` : DATA.devices[device],
          data: points.map((p) => ({ x: +parseDate(p[0]), y: p[3][metric] / scale, point: p })),
          borderColor: colours[slot],
          backgroundColor: colours[slot],
          borderWidth: 2,
          borderDash: form ? DASHES[form].dash : [],
          borderCapStyle: form && DASHES[form].dash.length ? "butt" : "round",
          borderJoinStyle: "round",
          pointRadius: points.map((p, i) => (p[2] === false ? 5 : i === points.length - 1 ? 4 : 0)),
          pointHoverRadius: 5,
          pointHitRadius: 10,
          pointStyle: points.map((p) => (p[2] === false ? "crossRot" : "circle")),
          pointBorderColor: points.map((p) => (p[2] === false ? CRITICAL : surface)),
          pointBorderWidth: points.map((p) => (p[2] === false ? 2.5 : 2)),
          tension: 0,
        });
      });
    });

    const canvas = el("canvas", { role: "img",
      "aria-label": `${title}, ${caption} ${metric}, by run on ${datasets.map((d) => d.label).join("; ")}; ` +
        "the latest values are listed above it, and the history below holds every value" });
    const card = el("article", { class: "iron-trend" },
      el("header", {},
        el("a", { class: "iron-trend-name", href, textContent: title, title: `Open ${name}'s history` }),
        el("span", { class: "iron-trend-metric",
          textContent: `${caption[0].toUpperCase()}${caption.slice(1)}${unit ? ` (${unit})` : ""}${sense ? `, ${sense}` : ""}` })),
      el("ul", { class: "iron-trend-latest" }, ...rows),
      trend.group === "Operators" && oneShape
        ? el("small", { class: "iron-trend-what iron-trend-shape", textContent: oneShape, title: oneShape })
        : null,
      el("div", { class: "iron-trend-canvas" }, canvas));

    pending.push(() => {
      const ink = css("--md-default-fg-color--light");
      const grid = css("--md-default-fg-color--lightest");
      trendCharts.push(new Chart(canvas, {
        type: "line",
        data: { datasets },
        plugins: [crosshair],
        options: {
          animation: false,
          maintainAspectRatio: false,
          layout: { padding: { top: 6, right: 6 } },
          interaction: { mode: "ironRun", intersect: false },
          font: { family: getComputedStyle(document.body).fontFamily },
          scales: {
            x: {
              type: "linear",
              min: domain[0],
              max: domain[1],
              grid: { display: false },
              border: { color: grid },
              ticks: { color: ink, maxTicksLimit: 4, maxRotation: 0, callback: (v) => dayFmt.format(new Date(v)) },
            },
            y: {
              beginAtZero: true,
              grid: { color: grid },
              border: { display: false },
              ticks: { color: ink, maxTicksLimit: 4, callback: (v) => compact.format(v) },
            },
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                title: (items) => stamp(items[0].raw.point[0]).slice(0, 10),
                label: (item) => {
                  const p = item.raw.point;
                  return ` ${brief.format(p[3][metric] / scale)}${unit ? ` ${unit}` : ""}  ${item.dataset.label}` +
                    `${p[2] === false ? "  ✕ checks failed" : ""}`;
                },
                footer: () => "Click for the history",
                labelPointStyle: () => ({ pointStyle: "line", rotation: 0 }),
              },
              usePointStyle: true,
            },
          },
          onHover: (event, elements) => {
            event.native.target.style.cursor = elements.length ? "pointer" : "default";
          },
          onClick: () => openHistory(href),
        },
      }));
    });
    return card;
  }

  function formKey(members) {
    const used = new Set(members.flatMap((t) => t.series.map((line) => line.form)).filter(Boolean));
    const forms = Object.keys(DATA.forms).filter((form) => used.has(form));
    if (!forms.length) return null;
    const ink = css("--md-default-fg-color--light");
    return el("dl", { class: "iron-form-key" }, ...forms.flatMap((form) => [
      el("dt", {}, key(ink, form), form),
      el("dd", { textContent: DATA.forms[form] }),
    ]));
  }

  function drawTrends() {
    trendCharts.forEach((c) => c.destroy());
    trendCharts = [];
    const colours = PALETTE[scheme()];
    const devices = Object.keys(DATA.devices);
    const DAY = 8.64e7;
    const dayFull = new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", year: "numeric", timeZone: "UTC" });

    const pending = [];
    const groups = ["Models", "Operators"].flatMap((group) => {
      const members = DATA.trends.filter((t) => t.group === group);
      if (!members.length) return [];
      const times = members.flatMap((t) => t.series.flatMap(({ device, label }) =>
        seriesOf(t.benchmark, t.suite, label).devices[device].points
          .filter((p) => t.metric in p[3]).map((p) => +parseDate(p[0]))));
      const lo = Math.floor(Math.min(...times) / DAY) * DAY;
      const domain = [lo, Math.max(Math.ceil(Math.max(...times) / DAY) * DAY, lo + DAY)];
      const suites = [...new Set(members.map((t) => DATA.suites[t.suite].name.toLowerCase()))];
      return [
        el("h3", {}, group, el("small", { class: "iron-trend-span",
          textContent: `${suites.join(" and ")} suite, ${dayFmt.format(new Date(domain[0]))} to ${dayFull.format(new Date(domain[1] - 1))}` })),
        el("div", { class: "iron-trend-grid" }, ...members.map((t) => trendCard(t, devices, colours, domain, pending))),
        formKey(members),
      ].filter(Boolean);
    });
    trendsHost.replaceChildren(
      el("div", { class: "iron-trend-legend" },
        ...devices.map((d, slot) => el("span", { class: "iron-trend-device" }, key(colours[slot]), DATA.devices[d])),
        el("span", { class: "iron-bench-note",
          textContent: "Each card follows one headline figure; select one for every parametrization and metric." })),
      ...groups);
    pending.forEach((make) => make());
  }

  // ── Latest runs ──────────────────────────────────────────────────────────

  function runCell(run) {
    const better = run.moved.filter((m) => m[4] === "better").length;
    const worse = run.moved.length - better;
    const status = run.failed
      ? el("span", {}, el("span", { class: "iron-mark iron-worse", textContent: "✕" }), ` ${run.failed} of ${run.tests} failed`)
      : el("span", { textContent: `${run.tests} passed` });
    const when = el("small", { class: "iron-muted" }, `${stamp(run.date)}, ${age(run.date)} · `, commitLink(run.commit));
    if (!run.moved.length) {
      return [status, el("br"), when, el("br"), el("small", { class: "iron-muted", textContent: "Nothing moved past the gates" })];
    }
    const items = run.moved.map(([name, label, metric, pct, verdict]) =>
      el("li", {}, verdictMark(verdict), " ",
        el("a", { href: link(name, run.suite, metric), textContent: name }),
        ` · ${label} · ${metric} ${pct > 0 ? "+" : ""}${pct.toFixed(1)}%`));
    return [status, el("br"), when,
      el("details", { class: "iron-moved" },
        el("summary", { textContent: `Moved: ${better} better, ${worse} worse` }), el("ul", {}, ...items))];
  }

  function drawRuns() {
    const devices = Object.keys(DATA.devices);
    const suites = SUITE_ORDER.filter((s) => DATA.runs.some((r) => r.suite === s));
    const rows = suites.map((suite) => el("tr", {},
      el("th", { scope: "row", textContent: suiteName(suite) }),
      ...devices.map((device) => {
        const run = DATA.runs.find((r) => r.suite === suite && r.device === device);
        return el("td", {}, ...(run ? runCell(run) : [el("span", { class: "iron-muted", textContent: "—" })]));
      })));
    const table = el("table", {},
      el("thead", {}, el("tr", {}, el("th", { textContent: "Suite" }),
        ...devices.map((d) => el("th", { textContent: DATA.devices[d] })))),
      el("tbody", {}, ...rows));
    runsHost.replaceChildren(el("div", { class: "md-typeset__scrollwrap" },
      el("div", { class: "md-typeset__table iron-runs-table" }, table)),
      el("p", { class: "iron-bench-note",
        textContent: `Moved: past the gates since the run before. Page data built ${stamp(DATA.generated)}.` }));
  }

  // ── History ──────────────────────────────────────────────────────────────

  function fillNames() {
    const groups = { Models: [], Operators: [], "No longer run": [] };
    for (const [name, b] of Object.entries(DATA.benchmarks)) {
      groups[b.current ? b.group : "No longer run"].push(name);
    }
    pick.name.replaceChildren(...Object.entries(groups).filter(([, names]) => names.length)
      .map(([group, names]) => el("optgroup", { label: group },
        ...names.map((name) => el("option", { value: name, textContent: name })))));
  }

  function select(state) {
    const names = Object.keys(DATA.benchmarks);
    const first = (group) => names.find((n) => DATA.benchmarks[n].current && DATA.benchmarks[n].group === group);
    const featured = bench.dataset.default;
    const name = names.includes(state.bench) ? state.bench
      : names.includes(featured) && DATA.benchmarks[featured].current ? featured
      : first("Models") || first("Operators") || names[0];
    const b = DATA.benchmarks[name];
    const lead = DATA.trends.find((t) => t.benchmark === name);
    const suites = SUITE_ORDER.filter((s) => s in b.suites);
    const suite = suites.includes(state.suite) ? state.suite
      : lead && suites.includes(lead.suite) ? lead.suite : suites[0];
    const metrics = b.suites[suite].metrics;
    const metric = metrics.includes(state.metric) ? state.metric
      : lead && lead.suite === suite && metrics.includes(lead.metric) ? lead.metric : metrics[0];

    pick.name.value = name;
    pick.suite.replaceChildren(...suites.map((s) =>
      el("option", { value: s, textContent: DATA.suites[s].name })));
    pick.suite.value = suite;
    pick.metric.replaceChildren(...metrics.map((m) => el("option", { value: m, textContent: m })));
    pick.metric.value = metric;

    const view = `${name}\u0000${suite}`;
    if (view !== shown) {
      slots = new Map();
      shown = view;
    }
    const wanted = link(name, suite, metric);
    if (location.hash !== wanted) history.replaceState(null, "", wanted);
    draw(name, suite, metric);
  }

  function hasData(series, metric) {
    return Object.values(series.devices).some((d) => d.points.some((p) => metric in p[3]));
  }

  function draw(name, suite, metric) {
    const history = DATA.benchmarks[name].suites[suite];
    const series = history.series.filter((s) => hasData(s, metric));
    // Keep the drawn series that still have this metric; start from the
    // first ones still run when none do.
    for (const label of [...slots.keys()]) {
      if (!series.some((s) => s.label === label)) slots.delete(label);
    }
    if (!slots.size) {
      const current = series.filter((s) => Object.values(s.devices).some((d) => d.current));
      const leads = DATA.trends.filter((t) => t.benchmark === name && t.suite === suite);
      const headline = new Set(leads.flatMap((t) => t.series.map((line) => line.label)));
      const reach = (s) => Object.keys(s.devices).length;
      const lead = series.filter((s) => headline.has(s.label));
      [...(lead.length ? lead : current.length ? current : series)]
        .sort((a, b) => reach(b) - reach(a))
        .slice(0, PALETTE.light.length)
        .forEach((s, i) => slots.set(s.label, i));
    }

    const unit = unitOf(metric);
    const sense = direction(metric);
    const info = DATA.suites[suite];
    const docs = DATA.benchmarks[name].docs;
    about.replaceChildren(
      `${metric}${unit ? ` in ${unit}` : ""}${sense ? `, ${sense}` : ""}. ` +
      `${series.length} parametrization${series.length === 1 ? "" : "s"} in the ` +
      `${info.name.toLowerCase()} suite; up to ${PALETTE.light.length} are drawn at once.`,
      ...(docs ? [" ", el("a", { href: docs, textContent:
        DATA.benchmarks[name].group === "Models" ? "About the models" : `About ${name}` })] : []));

    drawCharts(series, metric);
    drawTable(series, metric, suite);
  }

  function scheme() {
    return document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "light";
  }

  function css(name) {
    return getComputedStyle(document.body).getPropertyValue(name).trim();
  }

  // A hairline at the pointer's run, so a reader aims at a date, not a line.
  const crosshair = {
    id: "ironCrosshair",
    afterDatasetsDraw(chart) {
      const active = chart.tooltip && chart.tooltip.getActiveElements();
      if (!active || !active.length) return;
      const x = active[0].element.x;
      const { top, bottom } = chart.chartArea;
      const ctx = chart.ctx;
      ctx.save();
      ctx.strokeStyle = css("--md-default-fg-color--lighter");
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x, top);
      ctx.lineTo(x, bottom);
      ctx.stroke();
      ctx.restore();
    },
  };

  function drawCharts(series, metric) {
    charts.forEach((c) => c.destroy());
    charts = [];
    chartsHost.replaceChildren();
    const colours = PALETTE[scheme()];
    const spread = DATA.spreads[metric];
    const drawn = series.filter((s) => slots.has(s.label));

    const devices = Object.keys(DATA.devices).filter((d) => series.some((s) => d in s.devices));
    const times = drawn.flatMap((s) => Object.values(s.devices)
      .flatMap((d) => d.points.filter((p) => metric in p[3]).map((p) => +parseDate(p[0]))));
    // Whole UTC days, so each tick names one day.
    const DAY = 8.64e7;
    const lo = Math.floor(Math.min(...times) / DAY) * DAY;
    const hi = Math.max(Math.ceil(Math.max(...times) / DAY) * DAY, lo + DAY);
    const step = DAY * Math.ceil((hi - lo) / DAY / 7);

    for (const device of devices) {
      const runs = new Set();
      const datasets = drawn.filter((s) => device in s.devices).map((s) => {
        const points = s.devices[device].points.filter((p) => metric in p[3]);
        points.forEach((p) => runs.add(p[0]));
        const colour = colours[slots.get(s.label)];
        const failed = points.map((p) => p[2] === false);
        return {
          label: s.label,
          data: points.map((p) => ({ x: +parseDate(p[0]), y: p[3][metric], point: p })),
          borderColor: colour,
          backgroundColor: colour,
          borderWidth: 2,
          pointRadius: failed.map((f) => (f ? 6 : 3)),
          pointHoverRadius: failed.map((f) => (f ? 8 : 5)),
          pointHitRadius: 12,
          pointStyle: failed.map((f) => (f ? "crossRot" : "circle")),
          pointBorderColor: failed.map((f) => (f ? CRITICAL : colour)),
          pointBorderWidth: failed.map((f) => (f ? 2.5 : 1)),
          tension: 0,
        };
      });

      const card = el("figure", { class: "iron-bench-chart" });
      card.append(el("figcaption", {}, el("strong", { textContent: DATA.devices[device] }),
        datasets.length ? ` · ${runs.size} run${runs.size === 1 ? "" : "s"}` : ""));
      chartsHost.append(card);
      if (!datasets.length) {
        card.append(el("p", { class: "iron-bench-note", textContent: `None of the drawn parametrizations ran on ${DATA.devices[device]}.` }));
        continue;
      }
      const box = el("div", { class: "iron-bench-canvas" });
      const canvas = el("canvas", { role: "img", "aria-label": `${metric} on ${DATA.devices[device]}, by run; the table below holds every value` });
      box.append(canvas);
      card.append(box);

      const ink = css("--md-default-fg-color--light");
      const grid = css("--md-default-fg-color--lightest");
      const unit = unitOf(metric);
      const sense = direction(metric);
      charts.push(new Chart(canvas, {
        type: "line",
        data: { datasets },
        plugins: [crosshair],
        options: {
          animation: false,
          maintainAspectRatio: false,
          interaction: { mode: "nearest", axis: "x", intersect: false },
          font: { family: getComputedStyle(document.body).fontFamily },
          scales: {
            x: {
              type: "linear",
              min: lo,
              max: hi,
              grid: { color: grid },
              border: { color: grid },
              ticks: { color: ink, stepSize: step, callback: (v) => dayFmt.format(new Date(v)) },
            },
            y: {
              beginAtZero: true,
              grid: { color: grid },
              border: { color: grid },
              ticks: { color: ink, callback: (v) => number(v) },
              title: { display: true, color: ink,
                       text: `${metric}${unit ? ` (${unit})` : ""}${sense ? ` · ${sense}` : ""}` },
            },
          },
          plugins: {
            legend: {
              position: "top",
              align: "start",
              labels: { color: ink, boxWidth: 18, boxHeight: 2, font: { size: 11 } },
              onClick: null,
            },
            tooltip: {
              callbacks: {
                title: (items) => {
                  const p = items[0].raw.point;
                  return `${stamp(p[0])} · ${p[1].slice(0, 7)}`;
                },
                label: (item) => {
                  const p = item.raw.point;
                  const mad = spread && spread in p[3] ? ` ± ${number(p[3][spread])} MAD` : "";
                  const fail = p[2] === false ? "  ✕ checks failed" : "";
                  return ` ${withUnit(p[3][metric], metric)}${mad}  ${item.dataset.label}${fail}`;
                },
                footer: () => "Click to open the commit",
              },
            },
          },
          onClick: (_, elements) => {
            if (!elements.length) return;
            const p = datasets[elements[0].datasetIndex].data[elements[0].index].point;
            window.open(`${DATA.repository}/commit/${p[1]}`, "_blank", "noopener");
          },
        },
      }));
    }
  }

  function drawTable(series, metric, suite) {
    const devices = Object.keys(DATA.devices).filter((d) => series.some((s) => d in s.devices));
    const colours = PALETTE[scheme()];
    const full = slots.size >= PALETTE.light.length;

    const head = el("tr", {}, el("th", { textContent: "Drawn" }), el("th", { textContent: "Parametrization" }),
      ...devices.flatMap((d) => [el("th", { textContent: `${DATA.devices[d]}` }),
                                 el("th", { textContent: "Change" })]));
    const rows = series.map((s) => {
      const slot = slots.get(s.label);
      const box = el("input", { type: "checkbox", checked: slot !== undefined,
                                disabled: slot === undefined && full,
                                "aria-label": `Draw ${s.label}` });
      box.addEventListener("change", () => {
        if (box.checked) {
          const used = new Set(slots.values());
          slots.set(s.label, [...PALETTE.light.keys()].find((i) => !used.has(i)));
        } else {
          slots.delete(s.label);
        }
        draw(pick.name.value, suite, metric);
      });
      const key = el("span", { class: "iron-key" });
      if (slot !== undefined) key.style.background = colours[slot];

      const cells = devices.flatMap((d) => {
        const run = s.devices[d];
        const points = run ? run.points.filter((p) => metric in p[3]) : [];
        if (!points.length) return [el("td", { class: "iron-muted", textContent: "—" }), el("td")];
        const last = points[points.length - 1];
        const value = el("td", { class: "iron-num" }, withUnit(last[3][metric], metric));
        if (last[2] === false) value.append(" ", el("span", { class: "iron-mark iron-worse", textContent: "✕", title: "Its checks failed" }));
        if (!run.current) value.append(el("br"), el("small", { class: "iron-muted", textContent: `last ran ${longDay.format(parseDate(last[0]))}` }));
        const moved = run.current ? run.changes[metric] : undefined;
        const change = el("td", { class: "iron-num" });
        if (moved) {
          const [pct, verdict] = moved;
          change.append(`${pct > 0 ? "+" : ""}${pct.toFixed(1)}%`);
          const mark = verdictMark(verdict);
          if (mark) change.append(" ", mark);
          else change.classList.add("iron-muted");
        }
        return [value, change];
      });
      return el("tr", {}, el("td", {}, el("label", { class: "iron-draw" }, box, key)),
        el("td", {}, el("span", { textContent: s.label, title: s.test })), ...cells);
    });
    tableHost.replaceChildren(el("div", { class: "md-typeset__scrollwrap" },
      el("div", { class: "md-typeset__table iron-bench-table" },
        el("table", {}, el("thead", {}, head), el("tbody", {}, ...rows)))),
      el("p", { class: "iron-bench-note",
        textContent: `Each device's latest ${metric}, and its change from the run before; ` +
          "a change inside the gates is greyed." }));
  }

  // ── Wiring ───────────────────────────────────────────────────────────────

  function start(data) {
    DATA = data;
    const deepLink = location.hash.includes("bench=");
    Chart.Interaction.modes.ironRun = eachRun;
    live.hidden = false;
    drawTrends();
    drawRuns();
    fillNames();
    select(hashState());
    pick.name.addEventListener("change", () => select({ bench: pick.name.value, metric: pick.metric.value }));
    pick.suite.addEventListener("change", () => select({ bench: pick.name.value, suite: pick.suite.value, metric: pick.metric.value }));
    pick.metric.addEventListener("change", () => select({ bench: pick.name.value, suite: pick.suite.value, metric: pick.metric.value }));
    window.addEventListener("hashchange", () => {
      select(hashState());
      bench.scrollIntoView({ behavior: "smooth" });
    });
    if (deepLink) bench.scrollIntoView();
    document.addEventListener("click", (event) => {
      const anchor = event.target.closest('a[href^="#bench="]');
      if (!anchor || event.defaultPrevented || event.button !== 0 ||
          event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      openHistory(anchor.getAttribute("href"));
    });
    new MutationObserver(() => {
      drawTrends();
      select(hashState());
    })
      .observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
  }

  fetch("data.json")
    .then((response) => {
      if (!response.ok) throw new Error(`data.json: ${response.status}`);
      return response.json();
    })
    .then(start)
    .catch((error) => console.info("Benchmarks: no data in this build.", error));
})();
