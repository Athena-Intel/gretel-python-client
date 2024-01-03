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

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, StrictStr


class UpdateConnectionRequest(BaseModel):
    """
    Request message for `UpdateConnection` Next Tag: 8
    """

    name: Optional[StrictStr] = None
    credentials: Optional[Dict[str, Any]] = Field(
        None,
        description="Plaintext credentials for the connection, to be encrypted in our cloud. This field may only be set if the existing connection's credentials are encrypted with a Gretel-managed key.",
    )
    encrypted_credentials: Optional[Dict[str, Any]] = Field(
        None,
        description="Pre-encrypted credentials for the connection, encrypted by a customer-managed key. This field may only be set if the existing connection's credentials are encrypted with a user-managed key.",
    )
    config: Optional[Dict[str, Any]] = None
    connection_target_type: Optional[StrictStr] = None
    __properties = [
        "name",
        "credentials",
        "encrypted_credentials",
        "config",
        "connection_target_type",
    ]

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
    def from_json(cls, json_str: str) -> UpdateConnectionRequest:
        """Create an instance of UpdateConnectionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateConnectionRequest:
        """Create an instance of UpdateConnectionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateConnectionRequest.parse_obj(obj)

        _obj = UpdateConnectionRequest.parse_obj(
            {
                "name": obj.get("name"),
                "credentials": obj.get("credentials"),
                "encrypted_credentials": obj.get("encrypted_credentials"),
                "config": obj.get("config"),
                "connection_target_type": obj.get("connection_target_type"),
            }
        )
        return _obj
