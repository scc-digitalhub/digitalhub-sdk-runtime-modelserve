# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from plugin_contract import check_plugin_package

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds


def test_every_declared_kind_is_registered() -> None:
    # It found the kubeaiserve and vllmserve kinds declared but not registered,
    # and two builder modules that could not be imported.
    check_plugin_package("digitalhub_runtime_modelserve", kinds=EntityKinds)
