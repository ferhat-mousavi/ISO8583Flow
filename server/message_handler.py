from iso8583 import Iso8583
from server.message_processor import ISO8583Message
from server.mti_definition import transaction_routes


class ISO8583MessageHandler(ISO8583Message):
    def __init__(self):
        super().__init__()

    def message_handler(self, request_message):
        self.set_request_message(request_message)

        # Log the incoming message (optional)
        print("Incoming ISO 8583 Message:")
        print(self.get_iso_request_message().getIsoContent())

        mti = self.get_iso_request_message().getMTI()
        processing_code = self.get_iso_request_message().getBit(3)

        transaction_key = (mti, processing_code)

        if transaction_key in transaction_routes:
            transaction_type = transaction_routes[transaction_key]
            match transaction_type:
                case "Sale":
                    self.process_sale()
                case "InstallmentSale":
                    self.process_installment_sale()
                case "PreAuthorization":
                    # Execute the logic for PreAuthorization transaction
                    self.process_pre_authorization()
                case "PostAuthorization":
                    # Execute the logic for PostAuthorization transaction
                    self.process_post_authorization()
                case "Refund":
                    # Execute the logic for Refund transaction
                    self.process_refund()
                case "PointInquiry":
                    # Execute the logic for Point Inquiry transaction
                    self.process_point_inquiry()
                case "IndependentRefund":
                    # Execute the logic for Independent Refund transaction
                    self.process_independent_refund()
                case "EndOfDay":
                    # Execute the logic for End of Day transaction
                    self.process_end_of_day()
                case "SaleCancellation":
                    # Execute the logic for Sale Cancellation transaction
                    self.process_sale_cancellation()
                case "PreAuthorizationCancellation":
                    # Execute the logic for PreAuthorization Cancellation transaction
                    self.process_pre_authorization_cancellation()
                case "PostAuthorizationCancellation":
                    # Execute the logic for PostAuthorization Cancellation transaction
                    self.process_post_authorization_cancellation()
                case "RefundCancellation":
                    # Execute the logic for Refund Cancellation transaction
                    self.process_refund_cancellation()
                case "IndependentRefundCancellation":
                    # Execute the logic for Independent Refund Cancellation transaction
                    self.process_independent_refund_cancellation()
                case "SocialSecurityPayment":
                    # Execute the logic for Social Security Payment transaction
                    self.process_social_security_payment()
                case "SocialSecurityPaymentCancellation":
                    # Execute the logic for Social Security Payment Cancellation transaction
                    self.process_social_security_payment_cancellation()
                case "SocialSecurityPaymentTechnicalCancel":
                    # Execute the logic for Social Security Payment Technical Cancel transaction
                    self.process_social_security_payment_technical_cancel()
                case "SocialSecurityPaymentCancelTechnicalCancel":
                    # Execute the logic for Social Security Payment Cancel Technical Cancel transaction
                    self.process_social_security_payment_cancel_technical_cancel()
                case "SaleTechnicalCancel":
                    # Execute the logic for Sale Technical Cancel transaction
                    self.process_sale_technical_cancel()
                case "PreAuthorizationTechnicalCancel":
                    # Execute the logic for PreAuthorization Technical Cancel transaction
                    self.process_pre_authorization_technical_cancel()
                case "PostAuthorizationTechnicalCancel":
                    # Execute the logic for PostAuthorization Technical Cancel transaction
                    self.process_post_authorization_technical_cancel()
                case "RefundTechnicalCancel":
                    # Execute the logic for Refund Technical Cancel transaction
                    self.process_refund_technical_cancel()
                case "IndependentRefundTechnicalCancel":
                    # Execute the logic for Independent Refund Technical Cancel transaction
                    self.process_independent_refund_technical_cancel()
                case "SaleCancellationTechnicalCancel":
                    # Execute the logic for Sale Cancellation Technical Cancel transaction
                    self.process_sale_cancellation_technical_cancel()
                case "PreAuthorizationCancellationTechnicalCancel":
                    # Execute the logic for PreAuthorization Cancellation Technical Cancel transaction
                    self.process_pre_authorization_cancellation_technical_cancel()
                case "PostAuthorizationCancellationTechnicalCancel":
                    # Execute the logic for PostAuthorization Cancellation Technical Cancel transaction
                    self.process_post_authorization_cancellation_technical_cancel()
                case "RefundCancellationTechnicalCancel":
                    # Execute the logic for Refund Cancellation Technical Cancel transaction
                    self.process_refund_cancellation_technical_cancel()
                case "IndependentRefundCancellationTechnicalCancel":
                    # Execute the logic for Independent Refund Cancellation Technical Cancel transaction
                    self.process_independent_refund_cancellation_technical_cancel()
                case _:
                    # Handle unknown transaction types
                    self.handle_unknown_transaction(mti)

        # Pack the message and return it
        return self.get_iso_response_message().getRawIso()

    def handle_unknown_transaction(self, mti):
        if len(mti) >= 3 and mti[2].isdigit():
            # Get the second character from the left and add 2
            new_third_digit = str(int(mti[2]) + 2)

            # Create the new string: replace the second character
            response_mti = mti[0:2] + new_third_digit + mti[3:]
        else:
            response_mti = mti  # If input is invalid, return the original string
        self.get_iso_response_message().setMTI(response_mti)  # Transaction response MTI
        self.get_iso_response_message().setBit(3, '000000')  # Processing code
        self.get_iso_response_message().setBit(39, '12')  # Invalid Transaction response code
