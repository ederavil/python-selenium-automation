from behave import given, when, then


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click Terms and Conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()


@when('Switch to new window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page opened')
def verify_tc_opened(context):
    context.app.tc_page.verify_tc_url()


@then('Close current page')
def close(context):
    context.app.tc_page.close()


@then('Return to original window')
def return_to_original_window(context):
    context.app.tc_page.switch_to_window_by_id(context.original_window)