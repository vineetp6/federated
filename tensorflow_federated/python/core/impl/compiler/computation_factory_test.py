# Copyright 2020, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest
import numpy as np

from tensorflow_federated.proto.v0 import computation_pb2 as pb
from tensorflow_federated.python.core.impl.compiler import computation_factory
from tensorflow_federated.python.core.impl.types import computation_types
from tensorflow_federated.python.core.impl.types import type_factory
from tensorflow_federated.python.core.impl.types import type_serialization


class CreateLambdaEmptyTupleTest(absltest.TestCase):

  def test_returns_coputation(self):
    proto = computation_factory.create_lambda_empty_struct()

    self.assertIsInstance(proto, pb.Computation)
    actual_type = type_serialization.deserialize_type(proto.type)
    expected_type = computation_types.FunctionType(
        None, computation_types.StructType(())
    )
    self.assertEqual(actual_type, expected_type)


class CreateLambdaIdentityTest(absltest.TestCase):

  def test_returns_computation_int(self):
    type_signature = computation_types.TensorType(np.int32)

    proto = computation_factory.create_lambda_identity(type_signature)

    self.assertIsInstance(proto, pb.Computation)
    actual_type = type_serialization.deserialize_type(proto.type)
    expected_type = type_factory.unary_op(type_signature)
    self.assertEqual(actual_type, expected_type)

  def test_returns_computation_tuple_unnamed(self):
    type_signature = computation_types.StructType([np.int32, np.float32])

    proto = computation_factory.create_lambda_identity(type_signature)

    self.assertIsInstance(proto, pb.Computation)
    actual_type = type_serialization.deserialize_type(proto.type)
    expected_type = type_factory.unary_op(type_signature)
    self.assertEqual(actual_type, expected_type)

  def test_returns_computation_tuple_named(self):
    type_signature = computation_types.StructType(
        [('a', np.int32), ('b', np.float32)]
    )

    proto = computation_factory.create_lambda_identity(type_signature)

    self.assertIsInstance(proto, pb.Computation)
    actual_type = type_serialization.deserialize_type(proto.type)
    expected_type = type_factory.unary_op(type_signature)
    self.assertEqual(actual_type, expected_type)

  def test_returns_computation_sequence(self):
    type_signature = computation_types.SequenceType(np.int32)

    proto = computation_factory.create_lambda_identity(type_signature)

    self.assertIsInstance(proto, pb.Computation)
    actual_type = type_serialization.deserialize_type(proto.type)
    expected_type = type_factory.unary_op(type_signature)
    self.assertEqual(actual_type, expected_type)


if __name__ == '__main__':
  absltest.main()
