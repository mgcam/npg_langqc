# Copyright (c) 2022 Genome Research Ltd.
#
# Author: Adam Blanchet <ab59@sanger.ac.uk>
#
# This file is part of npg_langqc.
#
# npg_langqc is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime

from pydantic import BaseModel, Field

from lang_qc.models.qc_state import QcState


class WellInfo(BaseModel):

    label: str = Field(
        default=None, title="Well label", description="The well identifier."
    )
    start: datetime = Field(default=None, title="Timestamp of well started")
    complete: datetime = Field(default=None, title="Timestamp of well complete")
    qc_status: QcState = Field(default=None, title="Well QC status")


class InboxResultEntry(BaseModel):

    run_name: str = Field(
        default=None,
        title="Run Name",
    )
    time_start: datetime = Field(default=None, title="Run start time")
    time_complete: datetime = Field(default=None, title="Run complete time")
    well: WellInfo
