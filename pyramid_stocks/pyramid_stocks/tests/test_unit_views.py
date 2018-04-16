def test_default_behavior_of_base_route(dummy_request):
    from ..views.default import index_view
    from pyramid.response import Response

    request = dummy_request
    response = index_view(request)
    assert isinstance(response, Response)
    assert response.text == 'I did a thing'


# def test_default_behavior_of_entries_views(dummy_request):
#     from ..views.default import entries.view

#     response = entries_view(dummy_request)
#     assert type(response) == dict
