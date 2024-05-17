class Sprite:
    def __init__(self, path,
            width_du = 1, height_du = 1,
            # Zero == same as du
            width_lr = 0, height_lr = 0,
            camera_du= "" , camera_lr = "same_as_du",
            is_rotatable=True, with_outline=True,
            lights="Object Lights",
            line_sets=["Object"],
            subset=[],
            skip_rotations=[]):
        self.path = path
        # width down & up
        self.width_du = width_du
        self.height_du = height_du
        # width left & right
        if (width_lr == 0):
            self.width_lr = width_du
        else:
            self.width_lr = width_lr
        if (height_lr == 0):
            self.height_lr = height_du
        else:
            self.height_lr = height_lr
        self.camera_du = camera_du
        if (camera_lr == "same_as_du"):
            self.camera_lr = camera_du
        else:
            self.camera_lr = camera_lr
        self.is_rotatable = is_rotatable
        self.with_outline = with_outline
        self.lights = lights
        self.line_sets = line_sets
        self.subset = subset
        self.skip_rotations = skip_rotations


SPRITES = {
    "Crawler.[N]Body01": Sprite("Beings/Bodies/Crawler.[N]Body01"),
    "Crawler.[N]Body01_1": Sprite("Beings/Bodies/Crawler.[N]Body01_1"),

    # Attached Crawler Hat
    "Human.[N]Crawler01": Sprite("Beings/Hats/Human.[N]Crawler01"),
    "Human.[N]Crawler01_": Sprite("Beings/Hats/Human.[N]Crawler01_", is_rotatable=False),
    "Human.[N]Crawler01_H": Sprite("Beings/Hats/Human.[N]Crawler01_H"),
}