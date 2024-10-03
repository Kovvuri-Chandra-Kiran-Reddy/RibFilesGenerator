package {shared_path}.{new_rib_package}.view

import {shared_path}.{new_rib_package}.{Rib}Params
import {shared_path}.{new_rib_package}.state.{Rib}State
import `in`.porter.kmputils.flux.base.BaseVMMapper

class {Rib}VMMapper : BaseVMMapper<{Rib}Params, {Rib}State, {Rib}VM>() {

  override fun map(params: {Rib}Params, state: {Rib}State) = {Rib}VM()
}