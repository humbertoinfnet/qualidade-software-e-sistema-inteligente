from flask import request, Response, current_app, json
from flask_openapi3 import Tag, APIBlueprint

from src.use_cases.application_score import Runner
from src.interface_adapters.schemas.application_score.application_score import (
    BodyApplicationScore,
    ResponseApplicationScore,
)
from src.interface_adapters.schemas.response import (
    ResponseError,
    ResponseSuccess,
    ResponseNoContent
)

tag = Tag(name="ApplicationScore", description="Rotas para classificação do Application Score")
blueprint = APIBlueprint(
    'application_score',
    __name__,
    abp_tags=[tag],
    doc_ui=True,
    abp_responses={
        200: ResponseSuccess,
        204: ResponseNoContent,
        500: ResponseError
    }
)

@blueprint.post(
    '/application-score',
    responses={200: ResponseApplicationScore}
)
def classify_application_score(body: BodyApplicationScore):
    """
    Rota POST para classificar application score
    """

    current_app.logger.info('[application-score] - acessa a rota POST /application-score')
    runner = Runner(body)
    data = runner.execute()

    return Response(
        json.dumps(data.to_dict('records'), ensure_ascii=False),
        mimetype="application/json",
        status=200,
    )
