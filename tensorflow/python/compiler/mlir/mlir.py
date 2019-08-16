# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""mlir is an experimental library that provides support APIs for MLIR."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.compiler.mlir.python.mlir_extension import import_graphdef
from tensorflow.python.util.tf_export import tf_export


@tf_export('mlir.experimental.convert_graph_def')
def convert_graph_def(graph_def):
  """Import a GraphDef and convert it to a textual MLIR module.

  Args:
    graph_def: An object of type graph_pb2.GraphDef or a string representation
      of a valid GraphDef.

  Returns:
    A textual representation of the MLIR module corresponding to the graphdef.
    Raises a RuntimeError on error.

  """
  return import_graphdef(str(graph_def))