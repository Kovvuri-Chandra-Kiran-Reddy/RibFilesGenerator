package {platform_path}.{new_rib_package}

import android.view.LayoutInflater
import android.view.ViewGroup
import com.theporter.android.customerapp.R
import com.theporter.android.customerapp.root.BaseRootComponent
import com.uber.rib.core.InteractorBaseComponent
import com.uber.rib.core.ViewBuilder
import dagger.Binds
import dagger.BindsInstance
import dagger.Provides
import {shared_path}.{new_rib_package}.{Rib}Listener
import {shared_path}.{new_rib_package}.{Rib}Params
import {shared_path}.{new_rib_package}.view.{Rib}Presenter
import javax.inject.Qualifier
import javax.inject.Scope

class {Rib}Builder(dependency: ParentComponent) :
  ViewBuilder<{Rib}View, {Rib}Router, {Rib}Builder.ParentComponent>(dependency) {
  fun build(parentViewGroup: ViewGroup, params: {Rib}Params, listener: {Rib}Listener): {Rib}Router {
    val view = createView(parentViewGroup)
    val interactorMP = {Rib}InteractorMPFactory.build(view, dependency, params, listener)
    val interactor = {Rib}Interactor(interactorMP)

    val component = Dagger{Rib}Builder_Component.builder()
      .parentComponent(dependency)
      .view(view)
      .interactor(interactor)
      .build()

    val router = component.router()
    interactorMP.router = router
    return router
  }

  override fun inflateView(inflater: LayoutInflater, parentViewGroup: ViewGroup): {Rib}View =
    inflater.inflate(R.layout.rib_{first_letter_small_rib_name}, parentViewGroup, false) as {Rib}View

  interface ParentComponent : BaseRootComponent

  @dagger.Module
  abstract class Module {

    @{Rib}Scope
    @Binds
    internal abstract fun presenter(view: {Rib}View): {Rib}Presenter

    @dagger.Module
    companion object {

      @{Rib}Scope
      @Provides
      @JvmStatic
      fun router(
        component: Component,
        view: {Rib}View,
        interactor: {Rib}Interactor,
      ): {Rib}Router = {Rib}Router(view, interactor, component)
    }
  }

  @{Rib}Scope
  @dagger.Component(modules = [Module::class], dependencies = [ParentComponent::class])
  interface Component : InteractorBaseComponent<{Rib}Interactor>, BuilderComponent {

    @dagger.Component.Builder
    interface Builder {
      @BindsInstance
      fun interactor(interactor: {Rib}Interactor): Builder

      @BindsInstance
      fun view(view: {Rib}View): Builder

      fun parentComponent(component: ParentComponent): Builder
      fun build(): Component
    }
  }

  interface BuilderComponent {
    fun router(): {Rib}Router
  }

  @Scope
  @Retention(AnnotationRetention.BINARY)
  internal annotation class {Rib}Scope

  @Qualifier
  @Retention(AnnotationRetention.BINARY)
  internal annotation class {Rib}Internal
}
