from scene import Scene

class SceneManager:
    def __init__(self, scenes:list[Scene], current_scene):
        self.scenes = scenes
        self.current_scene = current_scene
        self.old_scene = current_scene

    def get_scene_current_scene(self) -> Scene:
        return self.scenes[self.current_scene]
    
    def get_scene_by_name(self, name) -> Scene:
        for scene in self.scenes:
            if scene.name == name:
                return scene
            
        return Scene(name)
    
    def set_scene_by_name(self, name):
        self.current_scene = self.scenes.index(self.get_scene_by_name(name))