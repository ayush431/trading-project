import csv
from rest_framework.views import APIView
from common.django_utility import send_response
from MainApp.decorators import validate_params
from MainApp.models import CandleTable
from common.utility import format_date


class UploadCsvFileView(APIView):
    @validate_params(params=["csv_file"])
    def post(self, request):
        response_data = []
        description = None
        try:
            csv_file = request.FILES["csv_file"]
            print("cs", csv_file)
            candles_data = []

            decoded_file = csv_file.read().decode("utf-8").splitlines()
            # print("decode", decoded_file)
            # reader = csv.reader(decoded_file)
            # print("redader", reader)
            # next(reader, None)

            for index, row in enumerate(decoded_file):
                if index == 0:
                    continue

                data_row = row.split(",")
                candle = CandleTable(
                    date=format_date(data_row[1]),
                    open_price=data_row[3],
                    high_price=data_row[4],
                    low_price=data_row[5],
                    close_price=data_row[6],
                )
                candles_data.append(candle)

            result = CandleTable.objects.bulk_create(candles_data)
            if result:
                response_data = "Data Successfully created"
            exception_occured = False
        except Exception as error_msg:
            description = error_msg
            exception_occured = True
        finally:
            return send_response(
                exception_occured=exception_occured,
                custom_description=description,
                request=request,
                response_data=response_data,
            )
