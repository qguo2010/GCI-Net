from setuptools import setup, find_namespace_packages

setup(name='gciunet',
      packages=find_namespace_packages(include=["gciunet", "gciunet.*"]),
      install_requires=[
          "torch>=1.6.0a",
          "tqdm",
          "dicom2nifti",
          "scikit-image>=0.14",
          "medpy",
          "scipy",
          "batchgenerators>=0.21",
          "numpy",
          "sklearn",
          "SimpleITK",
          "pandas",
          "requests",
          "nibabel", 'tifffile'
      ],
      entry_points={
          'console_scripts': [
              'gci_unet_convert_decathlon_task = gciunet.experiment_planning.gci_unet_convert_decathlon_task:main',
              'gci_unet_plan_and_preprocess = gciunet.experiment_planning.gci_unet_plan_and_preprocess:main',
              'gci_unet_train = gciunet.run.run_training:main',
              'gci_unet_train_DP = gciunet.run.run_training_DP:main',
              'gci_unet_train_DDP = gciunet.run.run_training_DDP:main',
              'gci_unet_predict = gciunet.inference.predict_simple:main',
              'gci_unet_ensemble = gciunet.inference.ensemble_predictions:main',
              'gci_unet_find_best_configuration = gciunet.evaluation.model_selection.figure_out_what_to_submit:main',
              'gci_unet_print_available_pretrained_models = gciunet.inference.pretrained_models.download_pretrained_model:print_available_pretrained_models',
              'gci_unet_print_pretrained_model_info = gciunet.inference.pretrained_models.download_pretrained_model:print_pretrained_model_requirements',
              'gci_unet_download_pretrained_model = gciunet.inference.pretrained_models.download_pretrained_model:download_by_name',
              'gci_unet_download_pretrained_model_by_url = gciunet.inference.pretrained_models.download_pretrained_model:download_by_url',
              'gci_unet_determine_postprocessing = gciunet.postprocessing.consolidate_postprocessing_simple:main',
              'gci_unet_export_model_to_zip = gciunet.inference.pretrained_models.collect_pretrained_models:export_entry_point',
              'gci_unet_install_pretrained_model_from_zip = gciunet.inference.pretrained_models.download_pretrained_model:install_from_zip_entry_point',
              'gci_unet_change_trainer_class = gciunet.inference.change_trainer:main',
              'gci_unet_evaluate_folder = gciunet.evaluation.evaluator:gci_unet_evaluate_folder',
              'gci_unet_plot_task_pngs = gciunet.utilities.overlay_plots:entry_point_generate_overlay',
          ],
      },

      )