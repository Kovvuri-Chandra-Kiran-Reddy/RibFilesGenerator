package {platform_path}.{new_rib_package}

import com.uber.rib.core.RibInteractor
import {shared_path}.{new_rib_package}.view.{Rib}Presenter
import `in`.porter.kmputils.flux.components.base.interactor.BaseInteractorForAndroid

@RibInteractor
class {Rib}Interactor
constructor(
  interactorMP: {Rib}InteractorMP,
) : BaseInteractorForAndroid<{Rib}InteractorMP, {Rib}Presenter, {Rib}Router>(interactorMP)