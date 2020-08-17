from django.shortcuts import render
from .models import KanbanBoard, KanbanBoardElement
from django.http import JsonResponse, HttpResponse
from uuid import UUID

def kanban_board(request, id):
    board = KanbanBoard.objects.get(pk=id)
    board_elements = board.elements.all()
    
    return render(request, 'kanban_board/_board.html', 
        context={
            "kanban_board": board, 
            "kanban_board_elements": board_elements,
        })

def change_element_status(request):
    # check method
    if not request.method == "POST":
        return JsonResponse({"error": "bad_method", "details": "expected POST but got " + str(request.method)}, status=405)

    # get all required parameters
    parent_id = UUID(request.POST.get('kb_parent_id'))
    element_id = UUID(request.POST.get('kb_element_id'))
    new_status = request.POST.get('kb_new_status')

    # validate if all required parameters are present
    missing_params = []
    for param in [element_id, new_status, parent_id]:
        if param is None:
            missing_params.append(param)
    if len(missing_params) > 0:
        return JsonResponse({"error": "missing_parameters", "details": missing_params})

    # actual logic
    board = KanbanBoard.objects.get(pk=parent_id)
    el = board.elements.get(pk=element_id)
    el.kanban_board_state = new_status
    el.save()

    return HttpResponse(status=200)
    