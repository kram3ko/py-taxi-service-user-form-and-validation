from django.urls import path

from taxi.views import (
    AssignToCarView,
    CarCreateView,
    CarDeleteView,
    CarDetailView,
    CarsListView,
    CarUpdateView,
    DriverCreateView,
    DriverDeleteView,
    DriverDetailView,
    DriversListView,
    DriverUpdateView,
    HomePageView,
    ManufacturerCreateView,
    ManufacturerDeleteView,
    ManufacturerDetailView,
    ManufacturersListView,
    ManufacturerUpdateView,
)

app_name = "taxi"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path(
        "manufacturer/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/",
        ManufacturersListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturer/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail"
    ),
    path(
        "manufacturer/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"),
    path(
        "manufacturer/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"),
    path("car/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/", CarsListView.as_view(), name="car-list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("car/<int:pk>/assign/", AssignToCarView.as_view(), name="car-assign"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("driver/create", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/", DriversListView.as_view(), name="driver-list"),
    path(
        "driver/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "driver/<int:pk>/update/",
        DriverUpdateView.as_view(),
        name="driver-update"
    ),
    path(
        "deiver/<int:pk>/delete/",
        DriverDeleteView.as_view(),
        name="driver-delete"
    )
]
