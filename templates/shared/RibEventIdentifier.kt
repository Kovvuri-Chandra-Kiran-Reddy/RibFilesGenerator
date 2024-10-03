package {shared_path}.{new_rib_package}.analytics

import `in`.porter.customerapp.shared.analytics.centralanalytics.CustomerAppFlow
import `in`.porter.kmputils.analytics.events.EventIdentifiers
import `in`.porter.kmputils.analytics.events.ProductFlow

sealed class {Rib}EventIdentifier(
  override val isEnabled: Boolean = true,
  override val isDebug: Boolean = true,
  override val eventName: String,
  override val productFlow: ProductFlow = CustomerAppFlow.PROFILE, // update ur flow accordingly
) : EventIdentifiers