#    Copyright 2020 Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
from batchgenerators.utilities.file_and_folder_operations import maybe_mkdir_p, join

# do not modify these unless you know what you are doing
my_output_identifier = "gci_unet"
default_plans_identifier = "gci_unet_Plansv2.1"
default_data_identifier = 'gci_unet_Data_plans_v2.1'
default_trainer = "gci_unet_trainer_brain"

"""
PLEASE READ paths.md FOR INFORMATION TO HOW TO SET THIS UP
"""



base = os.environ['gci_unet_raw_data_base'] if "gci_unet_raw_data_base" in os.environ.keys() else None
preprocessing_output_dir = os.environ['gci_unet_preprocessed'] if "gci_unet_preprocessed" in os.environ.keys() else None
network_training_output_dir_base = os.path.join(os.environ['gci_unet_RESULTS_FOLDER']) if "gci_unet_RESULTS_FOLDER" in os.environ.keys() else None
#
if base is not None:
    gci_unet_raw_data = join(base, "gci_unet_raw_data")
    gci_unet_cropped_data = join(base, "gci_unet_cropped_data")
    maybe_mkdir_p(gci_unet_raw_data)
    maybe_mkdir_p(gci_unet_cropped_data)
else:
    print("gci_unet_raw_data_base is not defined and model can only be used on data for which preprocessed files "
          "are already present on your system. model cannot be used for experiment planning and preprocessing like "
          "this. If this is not intended, please read run_training_synapse.sh/run_training_acdc.sh "
          "for information on how to set this up properly.")
    gci_unet_cropped_data = gci_unet_raw_data = None

if preprocessing_output_dir is not None:
    maybe_mkdir_p(preprocessing_output_dir)
else:
    print("gci_unet_preprocessed is not defined and model can not be used for preprocessing "
          "or training. If this is not intended, please read documentation/setting_up_paths.md for "
          "information on how to set this up.")
    preprocessing_output_dir = None

if network_training_output_dir_base is not None:
    network_training_output_dir = join(network_training_output_dir_base, my_output_identifier)
    print('*'*20)
    print(network_training_output_dir)
    print('*'*20)
    maybe_mkdir_p(network_training_output_dir)
else:
    print("RESULTS_FOLDER is not defined and nnU-Net cannot be used for training or "
          "inference. If this is not intended behavior, please read run_training_synapse.sh/run_training_acdc.sh "
          "for information on how to set this up.")
    network_training_output_dir = None
