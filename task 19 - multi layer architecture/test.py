# -*- coding: utf-8 -*-


def test_cart_work(app):
    app.pickup_product()
    app.purchase_product()
    app.remove_invoice()
    assert app.is_invoice_removed
