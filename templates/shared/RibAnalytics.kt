package {shared_path}.{new_rib_package}.analytics

import `in`.porter.kmputils.analytics.EventRecorder
import `in`.porter.kmputils.analytics.FeatureAnalytics
import `in`.porter.kmputils.commons.inject.Inject

class {Rib}Analytics
@Inject
constructor(
  eventRecorder: EventRecorder,
) : FeatureAnalytics(eventRecorder)