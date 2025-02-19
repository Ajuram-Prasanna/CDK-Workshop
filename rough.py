s = """
		"codepipeline:ListPipelines",
                "codepipeline:GetPipeline",
                "codepipeline:GetPipelineState",
                "codepipeline:GetPipelineExecution",
                "codepipeline:GetPipelineExecutionHistory",
                "codepipeline:ListPipelineExecutions",
                "codepipeline:ListActionExecutions",
                "codepipeline:ListPipelineResources"
"""

s = s.replace('"', '')
s = s.replace('\n', '')
s = s.replace('\t', '')
s = s.replace(' ', '')
s = s.split(',')

for i in s:
    print(i)