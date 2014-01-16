# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Template file used by ExpGenerator to generate the actual
permutations.py file by replacing $XXXXXXXX tokens with desired values.

This permutations.py file was generated by:
$EXP_GENERATOR_PROGRAM_PATH
"""

import os

from nupic.swarming.permutationhelpers import *

# The name of the field being predicted.  Any allowed permutation MUST contain
# the prediction field.
# (generated from PREDICTION_FIELD)
predictedField = '$PREDICTION_FIELD'

$PERM_FIXED_FIELDS
$PERM_FAST_SWARM_MODEL_PARAMS

permutations = {
  'aggregationInfo': $PERM_AGGREGATION_CHOICES,

  'modelParams': {
    $PERM_INFERENCE_TYPE_CHOICES

    'sensorParams': {
      'encoders': {
        $PERM_ENCODER_CHOICES
      },
    },

    'spParams': {
      $PERM_SP_CHOICES
    },

    'tpParams': {
      $PERM_TP_CHOICES
    },

    'clParams': {
      $PERM_CL_CHOICES
    },
  }
}


# Fields selected for final hypersearch report;
# NOTE: These values are used as regular expressions by RunPermutations.py's
#       report generator
# (fieldname values generated from PERM_PREDICTED_FIELD_NAME)
report = [
          '.*$PREDICTION_FIELD.*',
         ]

# Permutation optimization setting: either minimize or maximize metric
# used by RunPermutations.
# NOTE: The value is used as a regular expressions by RunPermutations.py's
#       report generator
# (generated from $PERM_OPTIMIZE_SETTING)
$PERM_OPTIMIZE_SETTING

minParticlesPerSwarm = $HS_MIN_PARTICLES

$PERM_ALWAYS_INCLUDE_PREDICTED_FIELD

$PERM_MIN_FIELD_CONTRIBUTION
$PERM_KILL_USELESS_SWARMS
$PERM_MAX_FIELD_BRANCHING
$PERM_TRY_ALL_3_FIELD_COMBINATIONS
$PERM_TRY_ALL_3_FIELD_COMBINATIONS_W_TIMESTAMPS

$PERM_MAX_MODELS

#############################################################################
def permutationFilter(perm):
  """ This function can be used to selectively filter out specific permutation
  combinations. It is called by RunPermutations for every possible permutation
  of the variables in the permutations dict. It should return True for valid a
  combination of permutation values and False for an invalid one.

  Parameters:
  ---------------------------------------------------------
  perm: dict of one possible combination of name:value
        pairs chosen from permutations.
  """

  # An example of how to use this
  #if perm['__consumption_encoder']['maxval'] > 300:
  #  return False;
  #
  return True
