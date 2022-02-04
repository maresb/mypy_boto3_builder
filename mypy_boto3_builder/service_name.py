"""
Description for boto3 service.
"""
from typing import Literal

from mypy_boto3_builder.constants import (
    AIOBOTOCORE_MODULE_NAME,
    AIOBOTOCORE_PYPI_NAME,
    MODULE_NAME,
    PYPI_NAME,
)
from mypy_boto3_builder.utils.strings import get_anchor_link, is_reserved

__all__ = (
    "ServiceName",
    "ServiceNameCatalog",
)


class ServiceName:
    """
    Description for boto3 service.
    """

    ALL = "all"
    UPDATED = "updated"
    LATEST = "latest"
    ESSENTIAL = (
        "ec2",
        "rds",
        "s3",
        "lambda",
        "sqs",
        "cloudformation",
        "dynamodb",
    )
    CONDA_FORGE_AVAILABLE = (
        "ec2",
        "rds",
        "s3",
        "lambda",
        "sqs",
        "cloudformation",
        "dynamodb",
    )

    def __init__(self, name: str, class_name: str) -> None:
        self.name = name
        self.class_name = class_name
        self.boto3_version = self.LATEST

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f"<ServiceName {self.name} {self.class_name}>"

    @property
    def underscore_name(self) -> str:
        """
        Python-friendly service name.
        """
        return self.name.replace("-", "_")

    @property
    def boto3_name(self) -> str:
        """
        Boto3 package name.
        """
        return self.name

    @property
    def import_name(self) -> str:
        """
        Safe mudule import name.
        """
        name = self.name.replace("-", "_")
        if is_reserved(name):
            return f"{name}_"

        return name

    @property
    def module_name(self) -> str:
        """
        Package name for given service for boto3.
        """
        return f"{MODULE_NAME}_{self.underscore_name}"

    @property
    def aiobotocore_module_name(self) -> str:
        """
        Package name for given service for aiobotocore.
        """
        return f"{AIOBOTOCORE_MODULE_NAME}_{self.underscore_name}"

    @property
    def pypi_name(self) -> str:
        """
        Name of boto3 package on PyPI.
        """
        return f"{PYPI_NAME}-{self.name}"

    @property
    def aiobotocore_pypi_name(self) -> str:
        """
        Name of aiobotocore package on PyPI.
        """
        return f"{AIOBOTOCORE_PYPI_NAME}-{self.name}"

    @property
    def extras_name(self) -> str:
        """
        Extras name for subpackage installation.
        """
        return self.name

    def is_essential(self) -> bool:
        """
        Whether service is included to `boto3-stubs[essential]`.
        """
        return self.name in self.ESSENTIAL

    def is_conda_forge_available(self) -> bool:
        """
        Whether service is available for `conda-forge`.
        """
        return self.name in self.CONDA_FORGE_AVAILABLE

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            "https://boto3.amazonaws.com/v1/documentation/api/"
            f"latest/reference/services/{self.boto3_name}.html#{self.class_name}"
        )

    def get_boto3_doc_link(self, *parts: str) -> str:
        """
        Get link to boto3 docs with anchor.

        Arguments:
            parts -- Anchor parts
        """
        return ".".join([self.boto3_doc_link, *parts])

    @staticmethod
    def get_md_doc_link(
        file: Literal[
            "client",
            "service_resource",
            "waiters",
            "paginators",
            "type_defs",
            "literals",
        ],
        *parts: str,
    ) -> str:
        """
        Get link to MD docs with anchor.

        Arguments:
            file -- HTML file name
            parts -- Anchor parts
        """
        link = f"./{file}.md"
        if not parts:
            return link
        anchor = "".join([get_anchor_link(part) for part in parts])
        return f"{link}#{anchor}"


class ServiceNameCatalog:
    """
    Finder for boto3 services by name.
    """

    ec2 = ServiceName("ec2", "EC2")
    iam = ServiceName("iam", "IAM")
    s3 = ServiceName("s3", "S3")
    cloudwatch = ServiceName("cloudwatch", "CloudWatch")
    opsworks = ServiceName("opsworks", "OpsWorks")
    sns = ServiceName("sns", "SNS")
    glacier = ServiceName("glacier", "Glacier")
    dynamodb = ServiceName("dynamodb", "DynamoDB")
    sqs = ServiceName("sqs", "SQS")
    cloudformation = ServiceName("cloudformation", "CloudFormation")
    cloudsearchdomain = ServiceName("cloudsearchdomain", "CloudSearchDomain")
    logs = ServiceName("logs", "CloudWatchLogs")
    lambda_ = ServiceName("lambda", "Lambda")

    ITEMS: dict[str, ServiceName] = {
        ec2.name: ec2,
        iam.name: iam,
        s3.name: s3,
        cloudwatch.name: cloudwatch,
        opsworks.name: opsworks,
        sns.name: sns,
        glacier.name: glacier,
        dynamodb.name: dynamodb,
        sqs.name: sqs,
        cloudformation.name: cloudformation,
        cloudsearchdomain.name: cloudsearchdomain,
        logs.name: logs,
        lambda_.name: lambda_,
    }

    @classmethod
    def add(cls, name: str, class_name: str) -> ServiceName:
        """
        Add new ServiceName to catalog or modify existing one.

        Returns:
            New ServiceName or modified if it exists.
        """
        if name in cls.ITEMS:
            service_name = cls.ITEMS[name]
            service_name.class_name = class_name
            return service_name

        service_name = ServiceName(name, class_name)
        cls.ITEMS[name] = service_name
        return service_name
