package {platform_path}.{new_rib_package}

import {shared_path}.{new_rib_package}.{Rib}Listener
import {shared_path}.{new_rib_package}.{Rib}Params
import {shared_path}.{new_rib_package}.view.{Rib}Presenter

object {Rib}InteractorMPFactory {

  fun build(
    presenter: {Rib}Presenter,
    dependency: {Rib}Builder.ParentComponent,
    params: {Rib}Params,
    listener: {Rib}Listener,
  ): {Rib}InteractorMP = {Rib}BuilderMP().build(
      coroutineExceptionHandler = dependency.interactorCoroutineExceptionHandler(),
      presenter = presenter,
      listener = listener,
      params = params,
      appLanguageRepo = dependency.appLanguageRepo(),
      eventRecorder = dependency.eventRecorder(),
    )
}