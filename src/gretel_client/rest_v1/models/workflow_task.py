# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

from gretel_client.rest_v1.models.project import Project
from gretel_client.rest_v1.models.user_profile import UserProfile


class WorkflowTask(BaseModel):
    """
    Next Tag: 23
    """

    id: StrictStr = Field(...)
    workflow_run_id: StrictStr = Field(...)
    project_id: StrictStr = Field(...)
    project: Optional[Project] = None
    log_location: StrictStr = Field(...)
    status: StrictStr = Field(...)
    action_name: StrictStr = Field(
        ...,
        description="The user supplied name of the workflow action that produced this task. The name can be mapped back to the original workflow config.",
    )
    action_type: StrictStr = Field(
        ...,
        description="The type of workflow action running the task. Eg `s3_source` or `gretel_model`.",
    )
    error_msg: Optional[StrictStr] = Field(
        None,
        description="If the task is in an error state, this field will get populated with an error message suitable for displaying in the console. These error messages are meant to span a single line, and will be human readable.",
    )
    error_code: Optional[StrictInt] = Field(
        None,
        description="The code associated with an error message. These codes can be used to group like errors together.",
    )
    stack_trace: Optional[StrictStr] = Field(
        None,
        description="A more detailed stack trace that can be used for root cause analysis. This stack trace generally shouldn't be shown in the UI and will span many lines.",
    )
    created_by: StrictStr = Field(...)
    created_by_profile: Optional[UserProfile] = None
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    pending_at: Optional[datetime] = None
    active_at: Optional[datetime] = None
    error_at: Optional[datetime] = None
    lost_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    __properties = [
        "id",
        "workflow_run_id",
        "project_id",
        "project",
        "log_location",
        "status",
        "action_name",
        "action_type",
        "error_msg",
        "error_code",
        "stack_trace",
        "created_by",
        "created_by_profile",
        "created_at",
        "updated_at",
        "pending_at",
        "active_at",
        "error_at",
        "lost_at",
        "completed_at",
    ]

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "RUN_STATUS_UNKNOWN",
            "RUN_STATUS_CREATED",
            "RUN_STATUS_PENDING",
            "RUN_STATUS_ACTIVE",
            "RUN_STATUS_ERROR",
            "RUN_STATUS_LOST",
            "RUN_STATUS_COMPLETED",
            "RUN_STATUS_CANCELLING",
            "RUN_STATUS_CANCELLED",
        ):
            raise ValueError(
                "must be one of enum values ('RUN_STATUS_UNKNOWN', 'RUN_STATUS_CREATED', 'RUN_STATUS_PENDING', 'RUN_STATUS_ACTIVE', 'RUN_STATUS_ERROR', 'RUN_STATUS_LOST', 'RUN_STATUS_COMPLETED', 'RUN_STATUS_CANCELLING', 'RUN_STATUS_CANCELLED')"
            )
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WorkflowTask:
        """Create an instance of WorkflowTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict["project"] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by_profile
        if self.created_by_profile:
            _dict["created_by_profile"] = self.created_by_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowTask:
        """Create an instance of WorkflowTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowTask.parse_obj(obj)

        _obj = WorkflowTask.parse_obj(
            {
                "id": obj.get("id"),
                "workflow_run_id": obj.get("workflow_run_id"),
                "project_id": obj.get("project_id"),
                "project": Project.from_dict(obj.get("project"))
                if obj.get("project") is not None
                else None,
                "log_location": obj.get("log_location"),
                "status": obj.get("status"),
                "action_name": obj.get("action_name"),
                "action_type": obj.get("action_type"),
                "error_msg": obj.get("error_msg"),
                "error_code": obj.get("error_code"),
                "stack_trace": obj.get("stack_trace"),
                "created_by": obj.get("created_by"),
                "created_by_profile": UserProfile.from_dict(
                    obj.get("created_by_profile")
                )
                if obj.get("created_by_profile") is not None
                else None,
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "pending_at": obj.get("pending_at"),
                "active_at": obj.get("active_at"),
                "error_at": obj.get("error_at"),
                "lost_at": obj.get("lost_at"),
                "completed_at": obj.get("completed_at"),
            }
        )
        return _obj
