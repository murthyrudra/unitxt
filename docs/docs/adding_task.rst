.. _adding_task:

.. note::

   To use this tutorial, you need to :ref:`install unitxt <install_unitxt>`.


=====================================
Tasks 
=====================================

Tasks are fundamental to Unitxt, acting as a standardized interface for integrating new datasets, metrics and templates.

The Task schema is a formal definition of the NLP task, including its inputs, outputs, and default evaluation metrics.

The `input_fields` of the task are a set of fields that are used to format the textual input to the model.
The `reference_fields` of the task are a set of fields that are used to format the expected textual output from the model (gold references).
The `metrics` of the task are a set of default metrics to be used to evaluate the outputs of the model.

As an example, consider an evaluation task for LLMs to evaluate how well they are able to calculate the sum of two integer numbers.
The task is formally defined as:

.. code-block:: python

   from unitxt.blocks import Task

   task = Task(
        input_fields={"num1" : int, "num2" : int},
        reference_fields={"sum" : int},
        prediction_type=int,
        metrics=[
            "metrics.sum_accuracy",
            "metrics.sum_accuracy_approximate"
        ],
   )

The `input_fields` and `reference_fields` of the task are used to format the textual input to the model.

The task does not verbalize the input to the model, as this can be done in different ways by different templates.
For example, same input could be verbalized as

`How much is 303 plus 104?`

or as

`How much is three hundred and three plus one hundred and four?`

The `output` fields of the tasks are used to format the textual expected output from the model (gold references).
There may be a single gold reference or multiple.

The gold references are used in two places.  When running in-context learning, gold references are used as example answers.
The gold references are also passed to metrics that are reference based.

The `metrics` of the task are a set of default metrics to be used to evaluate the outputs of the model.

While language models generate textual predictions, the metrics often evaluate on different datatypes.  For example,
in this case, the metrics calculate the accuracy of the sum of two integers, expecting an integer prediction.
It is the responsibility of the templates, via its post processors to convert the model textual predictions
into the `prediction_type`.

A Task can define a `default_template` attribute that determines the default :ref:`Template <adding_template>` used to create the input to the model,
when the template is not explicitly specified by the user in the :ref:`Card <adding_dataset>`
definition or in the  :ref:`load_dataset <evaluating_datasets>` template argument.

.. code-block:: python

   from unitxt.blocks import Task
   from unitxt.templates import InputOutputTemplate

   template = InputOutputTemplate(
         input_format="How much is {num1} plus {num2}?",
         output_format="{sum}",
   )

   task = Task(
        input_fields={"num1" : int, "num2" : int},
        reference_fields={"sum" : int},
        prediction_type=int,
        metrics=[
            "metrics.sum_accuracy",
            "metrics.sum_accuracy_approximate"
        ],
        default_template=template
   )

To register the task to the catalog

.. code-block:: python

   from unitxt import add_to_catalog

   add_to_catalog(task,"tasks.calculator.sum")

