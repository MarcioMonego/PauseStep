from modules.core.props import Property, StepProperty
from modules.core.step import StepBase
from modules import cbpi

@cbpi.step
class PauseStep(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method. The class name must be unique in the system
    '''
    # Properties
    timer = Property.Number("Timer in Minutes", configurable=True)
    titleOfInitialMessage = Property.Text("Title of instruction message", configurable=True,default_value="Pause instruction",description="Title to show above the instruction messge")
    initialMessage = Property.Text("Instruction message", configurable=True, description="Message to show on begining of the Step.")

    def init(self):
        '''
        Initialize Step. This method is called once at the beginning of the step
        :return: 
        '''
        if not self.initialMessage == u'':
            self.initialMessage = self.initialMessage.encode("utf-8")
            self.titleOfInitialMessage = self.titleOfInitialMessage.encode("utf-8")
            self.notify(self.titleOfInitialMessage, self.initialMessage, timeout= int(self.timer)*1000*60)

    @cbpi.action("Start Timer Now")
    def start(self):
        '''
        Custom Action which can be execute form the brewing dashboard.
        All method with decorator @cbpi.action("YOUR CUSTOM NAME") will be available in the user interface
        :return: 
        '''
        self.stop_timer()
        self.start_timer(int(self.timer) * 60)

    def reset(self):
        self.stop_timer()

    #  def finish(self):
    #     pass

    def execute(self):

        if self.is_timer_finished() is None:
            self.start_timer(int(self.timer) * 60)

        # Check if timer finished and go to next step
        if self.is_timer_finished() == True:
            self.notify("End of Pause!", "Starting the next step", timeout=10000)
            self.next()