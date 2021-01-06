from pathlib import Path

data_dir = Path(__file__).parent / '../../data'

test_path = data_dir / 'test.csv'
train_path = data_dir / 'train.csv'
train_label_path = data_dir / 'train_label.csv'
test_nolabel_path = data_dir / 'test_nolabel.csv'

month_number = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

nominal = [
    'hotel',
    'is_canceled',
    'arrival_date_month',
    'arrival_date_week_number',
    'arrival_date_day_of_month',
    'country',
    'market_segment',
    'distribution_channel',
    'is_repeated_guest',
    'reserved_room_type',
    'assigned_room_type',
    'agent',
    'company',
    'customer_type',
    'reservation_status'
]
ordinal = ['meal', 'deposit_type']
interval = ['arrival_date_year']
ratio = [
    'lead_time',
    'stays_in_weekend_nights',
    'stays_in_week_nights',
    'adults',
    'children',
    'babies',
    'previous_cancellations',
    'previous_bookings_not_canceled',
    'booking_changes',
    'days_in_waiting_list',
    'adr',
    'required_car_parking_spaces',
    'total_of_special_requests'
]
meaningless = ['ID', 'reservation_status_date']
