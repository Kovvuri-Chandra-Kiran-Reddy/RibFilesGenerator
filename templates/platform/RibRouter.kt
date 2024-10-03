package {platform_path}.{new_rib_package}

import com.theporter.android.customerapp.base.rib.BaseViewRouter

class {Rib}Router(
  view: {Rib}View,
  interactor: {Rib}Interactor,
  component: {Rib}Builder.Component,
) : BaseViewRouter<{Rib}View, {Rib}Interactor, {Rib}Builder.Component>(
  view,
  interactor,
  component,
),
  {Rib}RouterMP