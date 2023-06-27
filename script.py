import boto3

# Cria um cliente do ECS
ecs_client = session.client('ecs')

# Obtém as tarefas em execução na zona sa-east-1b
cluster_name = 'ClusterXPTO'
service_name = 'servicexpto'
availability_zone = 'sa-east-1b'

response = ecs_client.list_tasks(
    cluster=cluster_name,
    serviceName=service_name,
    desiredStatus='RUNNING'
)

task_arns = response['taskArns']

# Para cada tarefa em execução, para a tarefa
for task_arn in task_arns:
    ecs_client.stop_task(
        cluster=cluster_name,
        task=task_arn
    )
    print(f"Stopped task: {task_arn}")