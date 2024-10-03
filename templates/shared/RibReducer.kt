package {shared_path}.{new_rib_package}.state

import `in`.porter.kmputils.flux.base.StateReducer
import kotlinx.coroutines.CoroutineDispatcher

class {Rib}Reducer(
  stateDispatcher: CoroutineDispatcher,
) : StateReducer<{Rib}State>(stateDispatcher) {

  override val initState: {Rib}State = {Rib}State()
}