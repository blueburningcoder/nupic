#! /usr/bin/env python
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
'~/nta/eng/lib/python2.6/site-packages/nupic/frameworks/opf/expGenerator/ExpGenerator.pyc'
"""

from nupic.swarming.permutationhelpers import *

# The name of the field being predicted.  Any allowed permutation MUST contain
# the prediction field.
# (generated from PREDICTION_FIELD)
predictedField = 'consumption'

ENC_WIDTH = 21

permutations = {
  'inferenceType': 'NontemporalMultiStep',
  'tpEnable': False,

  # Encoder permutation choices 
  # Example:
  #
  #  '__gym_encoder' : PermuteEncoder('gym', 'SDRCategoryEncoder', w=7,
  #        n=100),
  #                
  #  '__address_encoder' : PermuteEncoder('address', 'SDRCategoryEncoder', 
  #        w=7, n=100),
  #                
  #  '__timestamp_timeOfDay_encoder' : PermuteEncoder('timestamp', 
  #        'DateEncoder.timeOfDay', w=7, radius=PermuteChoices([1, 8])),
  #                
  #  '__timestamp_dayOfWeek_encoder' : PermuteEncoder('timestamp', 
  #        'DateEncoder.dayOfWeek', w=7, radius=PermuteChoices([1, 3])),
  #                
  #  '__consumption_encoder' : PermuteEncoder('consumption', 'ScalarEncoder', 
  #        w=7, n=PermuteInt(13, 500, 20), minval=0, 
  #        maxval=PermuteInt(100, 300, 25)),
  #            
  #  (generated from PERM_ENCODER_CHOICES)
  '__timestamp_timeOfDay_encoder' : PermuteEncoder(fieldName='timestamp', 
              encoderClass='DateEncoder.timeOfDay', 
              w=ENC_WIDTH, radius=PermuteFloat(0.5, 12)),
  '__timestamp_dayOfWeek_encoder' : PermuteEncoder(fieldName='timestamp', 
              encoderClass='DateEncoder.dayOfWeek', w=ENC_WIDTH, 
              radius=PermuteFloat(1, 6)),
  '__timestamp_weekend_encoder' : PermuteEncoder(fieldName='timestamp', 
              encoderClass='DateEncoder.weekend', w=ENC_WIDTH, 
              radius=PermuteChoices([1])),
  '__consumption_encoder' : PermuteEncoder(fieldName='consumption', 
              encoderClass='AdaptiveScalarEncoder', w=ENC_WIDTH, 
              n=PermuteInt(28, 521), clipInput=True),
  
  'tpSegmentActivationThreshold': 14,

  'tpMinSegmentMatchSynapseThreshold': 12,
}


# Fields selected for final hypersearch report;
# NOTE: These values are used as regular expressions by RunPermutations.py's
#       report generator
# (fieldname values generated from PERM_PREDICTED_FIELD_NAME)
report = [
          '.*consumption.*',
         ]

# Permutation optimization setting: either minimize or maximize metric
# used by RunPermutations.
# NOTE: The value is used as a regular expressions by RunPermutations.py's
#       report generator
# (generated from minimize = 'prediction:aae:window=1000:field=consumption')
minimize = "multiStepBestPredictions:multiStep:errorMetric='aae':steps=1:window=1000:field=consumption"



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
