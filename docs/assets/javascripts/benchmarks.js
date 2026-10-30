// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// The Benchmarks page: the suites' latest runs, and one benchmark's history
// per device, from the data.json ci/scripts/build_pages.py writes beside it.

(() => {
  const runsHost = document.getElementById("iron-runs");
  const bench = document.getElementById("iron-bench");
  if (!runsHost || !bench) return;

  // The data-viz reference palette, in its validated order: light and dark
  // steps of the same eight hues. A ninth series is never drawn at once.
  const PALETTE = {
    light: ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"],
    dark: ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767"],
  };
  const CRITICAL = "#d03b3b";
  const SUITE_ORDER = ["small", "examples", "extensive", "nightly"];

  const pick = { name: document.getElementById("iron-bench-name"),
                 suite: document.getElementById("iron-bench-suite"),
                 metric: document.getElementById("iron-bench-metric") };
  const about = document.getElementById("iron-bench-about");
  const chartsHost = document.getElementById("iron-bench-charts");
  const tableHost = document.getElementById("iron-bench-table");

  let DATA = null;
  let charts = [];
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

  // ── Latest runs ──────────────────────────────────────────────────────────

  function drawRuns() {
    const runs = [...DATA.runs].sort((a, b) =>
      SUITE_ORDER.indexOf(a.suite) - SUITE_ORDER.indexOf(b.suite) || a.device.localeCompare(b.device));
    const body = runs.map((run) => {
      const better = run.moved.filter((m) => m[4] === "better").length;
      const worse = run.moved.length - better;
      return el("tr", {},
        el("td", { textContent: suiteName(run.suite) }),
        el("td", { textContent: DATA.devices[run.device] || run.device }),
        el("td", {}, stamp(run.date), el("br"), el("small", { textContent: age(run.date) })),
        el("td", {}, commitLink(run.commit)),
        el("td", {}, run.failed
          ? el("span", {}, el("span", { class: "iron-mark iron-worse", textContent: "✕" }),
               ` ${run.failed} of ${run.tests} failed`)
          : `${run.tests} passed`),
        el("td", { textContent: run.moved.length ? `${better} better, ${worse} worse` : "none" }));
    });
    const table = el("table", {},
      el("thead", {}, el("tr", {}, ...["Suite", "Device", "Run", "Commit", "Tests", "Moved past the gates"]
        .map((h) => el("th", { textContent: h })))),
      el("tbody", {}, ...body));

    const details = runs.filter((run) => run.moved.length).map((run) => {
      const items = run.moved.map(([name, label, metric, pct, verdict]) =>
        el("li", {}, verdictMark(verdict), " ",
          el("a", { href: link(name, run.suite, metric), textContent: name }),
          ` · ${label} · ${metric} ${pct > 0 ? "+" : ""}${pct.toFixed(1)}%`));
      const worse = run.moved.some((m) => m[4] === "worse");
      return el("details", { class: worse ? "warning" : "success" },
        el("summary", { textContent: `${DATA.devices[run.device] || run.device}, ${suiteName(run.suite)}: ${run.moved.length} moved` }),
        el("ul", {}, ...items));
    });

    runsHost.replaceChildren(el("div", { class: "md-typeset__table" }, table), ...details,
      el("p", { class: "iron-bench-note", textContent: `Page data built ${stamp(DATA.generated)}.` }));
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
    const name = names.includes(state.bench) ? state.bench : first("Models") || first("Operators") || names[0];
    const b = DATA.benchmarks[name];
    const suites = SUITE_ORDER.filter((s) => s in b.suites);
    const suite = suites.includes(state.suite) ? state.suite : suites[0];
    const metrics = b.suites[suite].metrics;
    const metric = metrics.includes(state.metric) ? state.metric : metrics[0];

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
      const reach = (s) => Object.keys(s.devices).length;
      [...(current.length ? current : series)].sort((a, b) => reach(b) - reach(a))
        .slice(0, PALETTE.light.length)
        .forEach((s, i) => slots.set(s.label, i));
    }

    const unit = unitOf(metric);
    const sense = direction(metric);
    const info = DATA.suites[suite];
    about.textContent = `${metric}${unit ? ` in ${unit}` : ""}${sense ? `, ${sense}` : ""}. ` +
      `${series.length} parametrization${series.length === 1 ? "" : "s"} in the ` +
      `${info.name.toLowerCase()} suite; up to ${PALETTE.light.length} are drawn at once.`;

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
            legend: { display: false },
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
    tableHost.replaceChildren(el("div", { class: "md-typeset__table iron-bench-table" },
      el("table", {}, el("thead", {}, head), el("tbody", {}, ...rows))),
      el("p", { class: "iron-bench-note",
        textContent: `Each device's latest ${metric}, and its change from the run before; ` +
          "a change inside the gates is greyed." }));
  }

  // ── Wiring ───────────────────────────────────────────────────────────────

  function start(data) {
    DATA = data;
    bench.hidden = false;
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
    new MutationObserver(() => select(hashState()))
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
