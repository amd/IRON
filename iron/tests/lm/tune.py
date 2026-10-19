# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.tune``'s command line, device-free."""

import pytest

from iron.lm import Encoder, tune


def test_tuning_is_refused_without_a_profiles_directory(capsys):
    with pytest.raises(SystemExit):
        tune.main("encoder", Encoder, [])
    assert "no profiles directory" in capsys.readouterr().err
