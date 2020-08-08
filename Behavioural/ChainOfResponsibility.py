class Handler:
    def __init__(self, successor):
        self.successor = successor

    def handle(self, request):
        handled = self._handle(request)
        if not handled:
            print("-- Refering to successor,", request)
            self.successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("NotImplementedError")


class HandlerOne(Handler):
    def _handle(self, request):
        if 0 < request < 10:
            print("Handled by H-One", request)
            return True


class HandlerTwo(Handler):
    def _handle(self, request):
        if request < 25:
            print("Handled by H-Two", request)
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print("End of chain", request)
        return True


class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        for r in requests:
            self.handler.handle(r)


c = Client()
requests = [1, 2, 3, 24, 30]
c.delegate(requests)
