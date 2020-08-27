from aws_cdk import (
    core,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as actions
)


class PipelineCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sourceaction = actions.GitHubSourceAction(
            oauth_token=TOKENITÄHÄN,
            output=sourceoutput,
            owner="haimila",
            branch="master",
            repo=""


        )
        pipeline = codepipeline.Pipeline(
            self, "CodePipeline",
            pipeline_name="CDKPipelineTest"
        )

        pipeline.add_stage(
            stage_name="Source",
            actions=[

            ]
        )

