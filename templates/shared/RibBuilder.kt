package {shared_path}.{new_rib_package}

import `in`.porter.customerapp.shared.applanguage.repo.AppLanguageRepo
import {shared_path}.{new_rib_package}.analytics.{Rib}Analytics
import {shared_path}.{new_rib_package}.state.{Rib}Reducer
import {shared_path}.{new_rib_package}.view.{Rib}Presenter
import {shared_path}.{new_rib_package}.view.{Rib}VMMapper
import `in`.porter.kmputils.analytics.EventRecorder
import `in`.porter.kmputils.flux.base.interactor.InteractorDispatchersFactory
import `in`.porter.kmputils.flux.base.interactorv2.InteractorCoroutineExceptionHandler

class {Rib}Builder {
  fun build(
    coroutineExceptionHandler: InteractorCoroutineExceptionHandler,
    presenter: {Rib}Presenter,
    listener: {Rib}Listener,
    params: {Rib}Params,
    eventRecorder: EventRecorder,
    appLanguageRepo: AppLanguageRepo,
  ): {Rib}Interactor {
    val dispatchers = InteractorDispatchersFactory.createStateVMInteractorDispatcher()

    return {Rib}Interactor(
      dispatchers = dispatchers,
      coroutineExceptionHandler = coroutineExceptionHandler,
      appLanguageRepo = appLanguageRepo,
      presenter = presenter,
      reducer = {Rib}Reducer(dispatchers.stateDispatcher),
      listener = listener,
      vmMapper = {Rib}VMMapper(),
      params = params,
      analytics = {Rib}Analytics(eventRecorder),
    )
  }
}