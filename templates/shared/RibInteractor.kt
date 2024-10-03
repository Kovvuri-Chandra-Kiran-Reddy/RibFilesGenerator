package {shared_path}.{new_rib_package}

import `in`.porter.customerapp.shared.applanguage.repo.AppLanguageRepo
import {shared_path}.{new_rib_package}.analytics.{Rib}Analytics
import {shared_path}.{new_rib_package}.state.{Rib}Reducer
import {shared_path}.{new_rib_package}.state.{Rib}State
import {shared_path}.{new_rib_package}.view.{Rib}Presenter
import {shared_path}.{new_rib_package}.view.{Rib}VM
import {shared_path}.{new_rib_package}.view.{Rib}VMMapper
import `in`.porter.kmputils.flux.base.interactor.StateVMInteractorDispatchers
import `in`.porter.kmputils.flux.base.interactorv2.BaseStateVMInteractor
import `in`.porter.kmputils.flux.base.interactorv2.InteractorCoroutineExceptionHandler

class {Rib}Interactor(
  dispatchers: StateVMInteractorDispatchers,
  coroutineExceptionHandler: InteractorCoroutineExceptionHandler,
  appLanguageRepo: AppLanguageRepo,
  private val presenter: {Rib}Presenter,
  private val reducer: {Rib}Reducer,
  private val listener: {Rib}Listener,
  vmMapper: {Rib}VMMapper,
  private val params: {Rib}Params,
  private val analytics: {Rib}Analytics,
) : BaseStateVMInteractor<{Rib}Params, {Rib}State, {Rib}VM>(
  dispatchers,
  coroutineExceptionHandler,
  reducer,
  vmMapper,
  appLanguageRepo.values,
  presenter,
  params,
) {

  lateinit var router: {Rib}Router

  override fun didBecomeActive() {
    super.didBecomeActive()
  }
}