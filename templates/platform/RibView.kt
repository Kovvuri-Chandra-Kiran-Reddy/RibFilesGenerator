package {platform_path}.{new_rib_package}

import android.content.Context
import android.util.AttributeSet
import com.theporter.android.customerapp.databinding.Rib{Rib}Binding
import {shared_path}.{new_rib_package}.view.{Rib}Presenter
import {shared_path}.{new_rib_package}.view.{Rib}VM
import `in`.porter.kmputils.instrumentation.base.BaseFrameLayoutV2

class {Rib}View
@JvmOverloads
constructor(
  context: Context,
  attrs: AttributeSet? = null,
  defStyle: Int = 1,
) : BaseFrameLayoutV2<Rib{Rib}Binding>(
  context,
  attrs,
  defStyle,
  Rib{Rib}Binding::bind,
),
  {Rib}Presenter {

  override fun render(vm: {Rib}VM) {}
}