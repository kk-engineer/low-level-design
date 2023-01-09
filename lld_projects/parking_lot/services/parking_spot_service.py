from parking_lot.models import ParkingSpot, ParkingLot, ParkingFloor


class ParkingSpotService:

    def get_available_spot(self, lot: ParkingLot, floor: ParkingFloor) -> ParkingSpot:
        pass

    def mark_spot_booked(self, spot: ParkingSpot):
        pass
