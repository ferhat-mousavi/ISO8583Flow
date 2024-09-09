transaction_routes = {
    ("0200", "000000"): "Sale",  # Standard sale transaction where the payment is charged to the cardholder.

    ("0200", "120000"): "InstallmentSale",  # A sale where the payment is made in installments rather than a lump sum.

    ("0100", "300000"): "PreAuthorization",
    # A pre-authorization transaction to reserve funds on the cardholder's account, usually without completing the sale.

    ("0220", "020000"): "PostAuthorization",
    # A follow-up to the pre-authorization that completes the transaction by charging the cardholder.

    ("0200", "200000"): "Refund",
    # A transaction that refunds the cardholder for a previous sale, returning the funds to the card.

    ("0200", "400000"): "PointInquiry",
    # A query transaction to check the balance of loyalty points or rewards associated with the card.

    ("0200", "200001"): "IndependentRefund",
    # A refund that does not directly reference the original sale, usually processed independently.

    ("0500", "920000"): "EndOfDay",
    # A transaction used to close out the day's operations and settle all processed transactions.

    ("0420", "000000"): "SaleCancellation",
    # A cancellation of a previously completed sale transaction, effectively voiding it.

    ("0420", "300000"): "PreAuthorizationCancellation",
    # Cancels a previously issued pre-authorization, releasing any held funds.

    ("0420", "020000"): "PostAuthorizationCancellation",
    # Cancels a post-authorization, reversing the sale after the pre-authorization.

    ("0420", "200000"): "RefundCancellation",
    # Cancels a previously processed refund, ensuring the funds are not returned to the cardholder.

    ("0420", "200001"): "IndependentRefundCancellation",
    # Cancels an independent refund, reversing the refund that was processed without a direct reference.

    ("0200", "500000"): "SocialSecurityPayment",  # A payment made related to social security obligations.

    ("0420", "500000"): "SocialSecurityPaymentCancellation",  # Cancels a previously processed social security payment.

    ("0400", "500000"): "SocialSecurityPaymentTechnicalCancel",
    # A technical cancellation of a social security payment, typically due to system errors or other technical issues.

    ("0402", "500002"): "SocialSecurityPaymentCancelTechnicalCancel",
    # Cancels a previously processed technical cancellation of a social security payment.

    ("0400", "000000"): "SaleTechnicalCancel",
    # A technical cancellation of a sale, generally due to system or processing issues.

    ("0400", "300000"): "PreAuthorizationTechnicalCancel",
    # A technical cancellation of a pre-authorization, often due to technical failures.

    ("0400", "020000"): "PostAuthorizationTechnicalCancel",
    # A technical cancellation of a post-authorization, reversing the sale.

    ("0402", "200002"): "RefundTechnicalCancel",
    # A technical cancellation of a refund transaction, reversing it due to system issues.

    ("0402", "200003"): "IndependentRefundTechnicalCancel",
    # A technical cancellation of an independent refund, reversing the refund for technical reasons.

    ("0402", "000002"): "SaleCancellationTechnicalCancel",
    # A technical cancellation of a sale cancellation, restoring the original sale after a cancellation.

    ("0402", "300002"): "PreAuthorizationCancellationTechnicalCancel",
    # A technical cancellation of a pre-authorization cancellation, restoring the pre-authorization.

    ("0402", "020002"): "PostAuthorizationCancellationTechnicalCancel",
    # A technical cancellation of a post-authorization cancellation, restoring the post-authorization.

    ("0402", "200022"): "RefundCancellationTechnicalCancel",
    # A technical cancellation of a refund cancellation, restoring the refund process.

    ("0402", "200023"): "IndependentRefundCancellationTechnicalCancel"
    # A technical cancellation of an independent refund cancellation, reversing the cancellation process.
}
