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

from typing import Optional

from pydantic import BaseModel, StrictStr

from gretel_client.rest_v1.models.user_profile_image import UserProfileImage


class UserProfile(BaseModel):
    """
    Next Tag: 6
    """

    id: Optional[StrictStr] = None
    firstname: Optional[StrictStr] = None
    lastname: Optional[StrictStr] = None
    image: Optional[UserProfileImage] = None
    email: Optional[StrictStr] = None
    __properties = ["id", "firstname", "lastname", "image", "email"]

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
    def from_json(cls, json_str: str) -> UserProfile:
        """Create an instance of UserProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict["image"] = self.image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserProfile:
        """Create an instance of UserProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserProfile.parse_obj(obj)

        _obj = UserProfile.parse_obj(
            {
                "id": obj.get("id"),
                "firstname": obj.get("firstname"),
                "lastname": obj.get("lastname"),
                "image": (
                    UserProfileImage.from_dict(obj.get("image"))
                    if obj.get("image") is not None
                    else None
                ),
                "email": obj.get("email"),
            }
        )
        return _obj
