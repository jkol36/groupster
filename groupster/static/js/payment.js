$(function() {
  $('body').on("click", '.change-card, .subscribe-form button[type=submit]', function(e) {
    e.preventDefault();
    var $form = $(this).closest("form"),
        token = function(res) {
          $form.find("input[name=stripe_token]").val(res.id);
          $form.trigger("submit");
        };

    StripeCheckout.open({
      key:         $form.data("stripe-key"),
      name:        'Payment Method',
      panelLabel:  'Add Payment Method',
      token:       token
    });

    return false;
  });
});