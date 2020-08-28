from aws_cdk import (
    core,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as actions
)


class PipelineCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = codepipeline.Pipeline(
            self, "CodePipeline",
            pipeline_name="CDKPipelineTest"
        )
        token = core.SecretValue.secrets_manager("arn:aws:secretsmanager:ap-northeast-1:821383200340:secret:GitHubKey-LPPj2Z")
        sourceoutput = codepipeline.Artifact()
        sourceaction = actions.GitHubSourceAction(
            oauth_token=token,
            output=sourceoutput,
            owner="haimila",
            branch="master",
            repo="cfpipeline",
            action_name="SourceAction"
        )
        iam_capabilities = core.CfnCapabilities.NAMED_IAM
        templatepath = codepipeline.ArtifactPath(sourceoutput, "cfpipeline.yml")
        deployaction = actions.CloudFormationCreateUpdateStackAction(
            admin_permissions=True,
            stack_name="CdkPipelineStack",
            template_path=templatepath,
            replace_on_failure=True,
            action_name="DeployAction",
            capabilities=[iam_capabilities]
        )

        sourcestage = pipeline.add_stage(
            stage_name="Source",
            actions=[sourceaction]
        )

        pipeline.add_stage(
            stage_name="Deploy",
            actions=[deployaction],
            placement={"just_after": sourcestage}
        )

