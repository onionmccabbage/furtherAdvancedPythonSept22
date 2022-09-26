# the observer pattern is very popular just now
# when we have large or multiple data sets in rapid order, observables work well
# this is a 'publish-subscribe' model: wecreate an observable stram of data then one or more subscribers can observe it
# This way, the observable (publisher) is completely decoupled from all the subscribers

# we will create an observable (publisher) then subscribe to it to receive notifications
class NewsPublisher():
    # this is our observable
    def __init__(self):
        self.__subscribers = [] # start with an empty list for our subscribers
        self.__latest_news = None
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # remove the most recent subscriber
    def subscribers(self):
        # iterate over all current subscribers
        return [type(x).__name__ for x in self.__subscribers]
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()
    def add_news(self, news):
        self.__latest_news = news
    def get_news(self):
        return 'News: {}'.format(self.__latest_news)

# here are some subscribers to our observable
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.get_news())
class PrintSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.get_news())
class MediaSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.get_news())

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    # iterate over each subscriber, notifying of the news
    for Subscriber in [MediaSubscriber, PrintSubscriber, EmailSubscriber]:
        Subscriber(news_publisher) # we will have three subscribers to our news observable
        news_publisher.add_news('News flash - it\'s nearly lunchtime!!')
    news_publisher.notify_subscribers() # they all get notified