# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecWorkflow, TaskValidatorWorkflow


class TaskSpecKfpBuild(TaskSpecWorkflow):
    """
    TaskSpecKfpBuild specifications.
    """


class TaskValidatorKfpBuild(TaskValidatorWorkflow):
    """
    TaskValidatorKfpBuild validator.
    """
