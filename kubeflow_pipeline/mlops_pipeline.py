import kfp
from kfp import dsl

def data_processing_op():
    return dsl.ContainerOp(
        name='Data Processing',
        image='rishu0200/mycolorectal:latest',
        command=['python', 'src/data_processing.py']
    )

def model_training_op():
    return dsl.ContainerOp(
        name='Model Training',
        image='rishu0200/mycolorectal:latest',
        command=['python', 'src/model_training.py']
    )

###Pipline Definition
@dsl.pipeline(
    name='Colorectal Cancer Pipeline',
    description='Colorectal cancer detection pipeline.'
)
def colorectal_cancer_pipeline():
    data_processing = data_processing_op()
    
    model_training = model_training_op()
    model_training.after(data_processing)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(colorectal_cancer_pipeline, 'colorectal_cancer_pipeline.yaml')