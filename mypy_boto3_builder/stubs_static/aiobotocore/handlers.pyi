from typing import Any, Dict, Mapping

from botocore.signers import RequestSigner
from requests.models import Response

async def check_for_200_error(response: Response, **kwargs: Any) -> None: ...
async def inject_presigned_url_ec2(
    params: Mapping[str, Any], request_signer: RequestSigner, model: Any, **kwargs: Any
) -> None: ...
async def inject_presigned_url_rds(
    params: Mapping[str, Any], request_signer: RequestSigner, model: Any, **kwargs: Any
) -> None: ...
async def parse_get_bucket_location(
    parsed: Dict[str, Any], http_response: Response, **kwargs: Any
) -> None: ...
