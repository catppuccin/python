"""Catppuccin palette definition."""

from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette

PALETTE = Palette(
    latte=Flavor(
        name="Latte",
        identifier="latte",
        order=0,
        dark=False,
        colors=FlavorColors(
            rosewater=Color(
                name="Rosewater",
                identifier="rosewater",
                accent=True,
                order=0,
                hex="#dc8a78",
                rgb=RGB(r=220, g=138, b=120),
                hsl=HSL(
                    h=10.799999999999995, s=0.5882352941176472, l=0.6666666666666667
                ),
            ),
            flamingo=Color(
                name="Flamingo",
                identifier="flamingo",
                accent=True,
                order=1,
                hex="#dd7878",
                rgb=RGB(r=221, g=120, b=120),
                hsl=HSL(h=0, s=0.5976331360946746, l=0.6686274509803922),
            ),
            pink=Color(
                name="Pink",
                identifier="pink",
                accent=True,
                order=2,
                hex="#ea76cb",
                rgb=RGB(r=234, g=118, b=203),
                hsl=HSL(
                    h=316.0344827586207, s=0.7341772151898731, l=0.6901960784313725
                ),
            ),
            mauve=Color(
                name="Mauve",
                identifier="mauve",
                accent=True,
                order=3,
                hex="#8839ef",
                rgb=RGB(r=136, g=57, b=239),
                hsl=HSL(
                    h=266.0439560439561, s=0.8504672897196262, l=0.5803921568627451
                ),
            ),
            red=Color(
                name="Red",
                identifier="red",
                accent=True,
                order=4,
                hex="#d20f39",
                rgb=RGB(r=210, g=15, b=57),
                hsl=HSL(
                    h=347.0769230769231, s=0.8666666666666666, l=0.4411764705882353
                ),
            ),
            maroon=Color(
                name="Maroon",
                identifier="maroon",
                accent=True,
                order=5,
                hex="#e64553",
                rgb=RGB(r=230, g=69, b=83),
                hsl=HSL(h=354.78260869565213, s=0.76303317535545, l=0.5862745098039216),
            ),
            peach=Color(
                name="Peach",
                identifier="peach",
                accent=True,
                order=6,
                hex="#fe640b",
                rgb=RGB(r=254, g=100, b=11),
                hsl=HSL(
                    h=21.975308641975307, s=0.9918367346938776, l=0.5196078431372549
                ),
            ),
            yellow=Color(
                name="Yellow",
                identifier="yellow",
                accent=True,
                order=7,
                hex="#df8e1d",
                rgb=RGB(r=223, g=142, b=29),
                hsl=HSL(
                    h=34.948453608247426, s=0.7698412698412698, l=0.49411764705882355
                ),
            ),
            green=Color(
                name="Green",
                identifier="green",
                accent=True,
                order=8,
                hex="#40a02b",
                rgb=RGB(r=64, g=160, b=43),
                hsl=HSL(
                    h=109.23076923076923, s=0.5763546798029556, l=0.39803921568627454
                ),
            ),
            teal=Color(
                name="Teal",
                identifier="teal",
                accent=True,
                order=9,
                hex="#179299",
                rgb=RGB(r=23, g=146, b=153),
                hsl=HSL(
                    h=183.23076923076923, s=0.7386363636363636, l=0.34509803921568627
                ),
            ),
            sky=Color(
                name="Sky",
                identifier="sky",
                accent=True,
                order=10,
                hex="#04a5e5",
                rgb=RGB(r=4, g=165, b=229),
                hsl=HSL(
                    h=197.0666666666667, s=0.965665236051502, l=0.45686274509803926
                ),
            ),
            sapphire=Color(
                name="Sapphire",
                identifier="sapphire",
                accent=True,
                order=11,
                hex="#209fb5",
                rgb=RGB(r=32, g=159, b=181),
                hsl=HSL(
                    h=188.85906040268458, s=0.6995305164319249, l=0.4176470588235294
                ),
            ),
            blue=Color(
                name="Blue",
                identifier="blue",
                accent=True,
                order=12,
                hex="#1e66f5",
                rgb=RGB(r=30, g=102, b=245),
                hsl=HSL(
                    h=219.90697674418607, s=0.9148936170212768, l=0.5392156862745098
                ),
            ),
            lavender=Color(
                name="Lavender",
                identifier="lavender",
                accent=True,
                order=13,
                hex="#7287fd",
                rgb=RGB(r=114, g=135, b=253),
                hsl=HSL(
                    h=230.93525179856115, s=0.9720279720279721, l=0.7196078431372549
                ),
            ),
            text=Color(
                name="Text",
                identifier="text",
                accent=False,
                order=14,
                hex="#4c4f69",
                rgb=RGB(r=76, g=79, b=105),
                hsl=HSL(
                    h=233.79310344827587, s=0.16022099447513813, l=0.3549019607843137
                ),
            ),
            subtext1=Color(
                name="Subtext 1",
                identifier="subtext1",
                accent=False,
                order=15,
                hex="#5c5f77",
                rgb=RGB(r=92, g=95, b=119),
                hsl=HSL(
                    h=233.33333333333334, s=0.1279620853080569, l=0.4137254901960784
                ),
            ),
            subtext0=Color(
                name="Subtext 0",
                identifier="subtext0",
                accent=False,
                order=16,
                hex="#6c6f85",
                rgb=RGB(r=108, g=111, b=133),
                hsl=HSL(
                    h=232.79999999999998, s=0.10373443983402494, l=0.4725490196078431
                ),
            ),
            overlay2=Color(
                name="Overlay 2",
                identifier="overlay2",
                accent=False,
                order=17,
                hex="#7c7f93",
                rgb=RGB(r=124, g=127, b=147),
                hsl=HSL(
                    h=232.17391304347825, s=0.09623430962343092, l=0.5313725490196078
                ),
            ),
            overlay1=Color(
                name="Overlay 1",
                identifier="overlay1",
                accent=False,
                order=18,
                hex="#8c8fa1",
                rgb=RGB(r=140, g=143, b=161),
                hsl=HSL(
                    h=231.42857142857144, s=0.10047846889952144, l=0.5901960784313726
                ),
            ),
            overlay0=Color(
                name="Overlay 0",
                identifier="overlay0",
                accent=False,
                order=19,
                hex="#9ca0b0",
                rgb=RGB(r=156, g=160, b=176),
                hsl=HSL(
                    h=228.00000000000003, s=0.11235955056179768, l=0.6509803921568628
                ),
            ),
            surface2=Color(
                name="Surface 2",
                identifier="surface2",
                accent=False,
                order=20,
                hex="#acb0be",
                rgb=RGB(r=172, g=176, b=190),
                hsl=HSL(
                    h=226.6666666666667, s=0.12162162162162159, l=0.7098039215686275
                ),
            ),
            surface1=Color(
                name="Surface 1",
                identifier="surface1",
                accent=False,
                order=21,
                hex="#bcc0cc",
                rgb=RGB(r=188, g=192, b=204),
                hsl=HSL(
                    h=225.00000000000003, s=0.13559322033898308, l=0.7686274509803922
                ),
            ),
            surface0=Color(
                name="Surface 0",
                identifier="surface0",
                accent=False,
                order=22,
                hex="#ccd0da",
                rgb=RGB(r=204, g=208, b=218),
                hsl=HSL(
                    h=222.85714285714292, s=0.1590909090909089, l=0.8274509803921568
                ),
            ),
            base=Color(
                name="Base",
                identifier="base",
                accent=False,
                order=23,
                hex="#eff1f5",
                rgb=RGB(r=239, g=241, b=245),
                hsl=HSL(
                    h=220.00000000000009, s=0.23076923076923136, l=0.9490196078431372
                ),
            ),
            mantle=Color(
                name="Mantle",
                identifier="mantle",
                accent=False,
                order=24,
                hex="#e6e9ef",
                rgb=RGB(r=230, g=233, b=239),
                hsl=HSL(
                    h=220.00000000000006, s=0.21951219512195116, l=0.919607843137255
                ),
            ),
            crust=Color(
                name="Crust",
                identifier="crust",
                accent=False,
                order=25,
                hex="#dce0e8",
                rgb=RGB(r=220, g=224, b=232),
                hsl=HSL(
                    h=220.00000000000006, s=0.20689655172413762, l=0.8862745098039215
                ),
            ),
        ),
    ),
    frappe=Flavor(
        name="Frappé",
        identifier="frappe",
        order=1,
        dark=True,
        colors=FlavorColors(
            rosewater=Color(
                name="Rosewater",
                identifier="rosewater",
                accent=True,
                order=0,
                hex="#f2d5cf",
                rgb=RGB(r=242, g=213, b=207),
                hsl=HSL(h=10.2857142857143, s=0.5737704918032784, l=0.8803921568627451),
            ),
            flamingo=Color(
                name="Flamingo",
                identifier="flamingo",
                accent=True,
                order=1,
                hex="#eebebe",
                rgb=RGB(r=238, g=190, b=190),
                hsl=HSL(h=0, s=0.5853658536585367, l=0.8392156862745098),
            ),
            pink=Color(
                name="Pink",
                identifier="pink",
                accent=True,
                order=2,
                hex="#f4b8e4",
                rgb=RGB(r=244, g=184, b=228),
                hsl=HSL(h=316, s=0.7317073170731713, l=0.8392156862745098),
            ),
            mauve=Color(
                name="Mauve",
                identifier="mauve",
                accent=True,
                order=3,
                hex="#ca9ee6",
                rgb=RGB(r=202, g=158, b=230),
                hsl=HSL(
                    h=276.66666666666663, s=0.5901639344262294, l=0.7607843137254902
                ),
            ),
            red=Color(
                name="Red",
                identifier="red",
                accent=True,
                order=4,
                hex="#e78284",
                rgb=RGB(r=231, g=130, b=132),
                hsl=HSL(
                    h=358.8118811881188, s=0.6778523489932885, l=0.7078431372549019
                ),
            ),
            maroon=Color(
                name="Maroon",
                identifier="maroon",
                accent=True,
                order=5,
                hex="#ea999c",
                rgb=RGB(r=234, g=153, b=156),
                hsl=HSL(
                    h=357.77777777777777, s=0.6585365853658534, l=0.7588235294117647
                ),
            ),
            peach=Color(
                name="Peach",
                identifier="peach",
                accent=True,
                order=6,
                hex="#ef9f76",
                rgb=RGB(r=239, g=159, b=118),
                hsl=HSL(h=20.33057851239669, s=0.7908496732026143, l=0.7),
            ),
            yellow=Color(
                name="Yellow",
                identifier="yellow",
                accent=True,
                order=7,
                hex="#e5c890",
                rgb=RGB(r=229, g=200, b=144),
                hsl=HSL(
                    h=39.52941176470588, s=0.6204379562043796, l=0.7313725490196079
                ),
            ),
            green=Color(
                name="Green",
                identifier="green",
                accent=True,
                order=8,
                hex="#a6d189",
                rgb=RGB(r=166, g=209, b=137),
                hsl=HSL(
                    h=95.83333333333331, s=0.4390243902439024, l=0.6784313725490196
                ),
            ),
            teal=Color(
                name="Teal",
                identifier="teal",
                accent=True,
                order=9,
                hex="#81c8be",
                rgb=RGB(r=129, g=200, b=190),
                hsl=HSL(
                    h=171.5492957746479, s=0.3922651933701657, l=0.6450980392156862
                ),
            ),
            sky=Color(
                name="Sky",
                identifier="sky",
                accent=True,
                order=10,
                hex="#99d1db",
                rgb=RGB(r=153, g=209, b=219),
                hsl=HSL(
                    h=189.09090909090907, s=0.47826086956521735, l=0.7294117647058823
                ),
            ),
            sapphire=Color(
                name="Sapphire",
                identifier="sapphire",
                accent=True,
                order=11,
                hex="#85c1dc",
                rgb=RGB(r=133, g=193, b=220),
                hsl=HSL(
                    h=198.62068965517244, s=0.5541401273885351, l=0.692156862745098
                ),
            ),
            blue=Color(
                name="Blue",
                identifier="blue",
                accent=True,
                order=12,
                hex="#8caaee",
                rgb=RGB(r=140, g=170, b=238),
                hsl=HSL(
                    h=221.6326530612245, s=0.7424242424242424, l=0.7411764705882353
                ),
            ),
            lavender=Color(
                name="Lavender",
                identifier="lavender",
                accent=True,
                order=13,
                hex="#babbf1",
                rgb=RGB(r=186, g=187, b=241),
                hsl=HSL(
                    h=238.90909090909093, s=0.6626506024096385, l=0.8372549019607842
                ),
            ),
            text=Color(
                name="Text",
                identifier="text",
                accent=False,
                order=14,
                hex="#c6d0f5",
                rgb=RGB(r=198, g=208, b=245),
                hsl=HSL(
                    h=227.2340425531915, s=0.7014925373134333, l=0.8686274509803922
                ),
            ),
            subtext1=Color(
                name="Subtext 1",
                identifier="subtext1",
                accent=False,
                order=15,
                hex="#b5bfe2",
                rgb=RGB(r=181, g=191, b=226),
                hsl=HSL(
                    h=226.66666666666669, s=0.43689320388349495, l=0.7980392156862746
                ),
            ),
            subtext0=Color(
                name="Subtext 0",
                identifier="subtext0",
                accent=False,
                order=16,
                hex="#a5adce",
                rgb=RGB(r=165, g=173, b=206),
                hsl=HSL(
                    h=228.29268292682926, s=0.2949640287769784, l=0.7274509803921569
                ),
            ),
            overlay2=Color(
                name="Overlay 2",
                identifier="overlay2",
                accent=False,
                order=17,
                hex="#949cbb",
                rgb=RGB(r=148, g=156, b=187),
                hsl=HSL(
                    h=227.69230769230768, s=0.22285714285714275, l=0.6568627450980392
                ),
            ),
            overlay1=Color(
                name="Overlay 1",
                identifier="overlay1",
                accent=False,
                order=18,
                hex="#838ba7",
                rgb=RGB(r=131, g=139, b=167),
                hsl=HSL(
                    h=226.66666666666669, s=0.16981132075471703, l=0.584313725490196
                ),
            ),
            overlay0=Color(
                name="Overlay 0",
                identifier="overlay0",
                accent=False,
                order=19,
                hex="#737994",
                rgb=RGB(r=115, g=121, b=148),
                hsl=HSL(
                    h=229.0909090909091, s=0.13360323886639683, l=0.515686274509804
                ),
            ),
            surface2=Color(
                name="Surface 2",
                identifier="surface2",
                accent=False,
                order=20,
                hex="#626880",
                rgb=RGB(r=98, g=104, b=128),
                hsl=HSL(
                    h=228.00000000000003, s=0.1327433628318584, l=0.44313725490196076
                ),
            ),
            surface1=Color(
                name="Surface 1",
                identifier="surface1",
                accent=False,
                order=21,
                hex="#51576d",
                rgb=RGB(r=81, g=87, b=109),
                hsl=HSL(
                    h=227.14285714285714, s=0.14736842105263157, l=0.37254901960784315
                ),
            ),
            surface0=Color(
                name="Surface 0",
                identifier="surface0",
                accent=False,
                order=22,
                hex="#414559",
                rgb=RGB(r=65, g=69, b=89),
                hsl=HSL(
                    h=230.00000000000003, s=0.15584415584415584, l=0.30196078431372547
                ),
            ),
            base=Color(
                name="Base",
                identifier="base",
                accent=False,
                order=23,
                hex="#303446",
                rgb=RGB(r=48, g=52, b=70),
                hsl=HSL(
                    h=229.0909090909091, s=0.18644067796610175, l=0.23137254901960785
                ),
            ),
            mantle=Color(
                name="Mantle",
                identifier="mantle",
                accent=False,
                order=24,
                hex="#292c3c",
                rgb=RGB(r=41, g=44, b=60),
                hsl=HSL(
                    h=230.52631578947367, s=0.18811881188118806, l=0.19803921568627453
                ),
            ),
            crust=Color(
                name="Crust",
                identifier="crust",
                accent=False,
                order=25,
                hex="#232634",
                rgb=RGB(r=35, g=38, b=52),
                hsl=HSL(
                    h=229.41176470588238, s=0.19540229885057467, l=0.17058823529411765
                ),
            ),
        ),
    ),
    macchiato=Flavor(
        name="Macchiato",
        identifier="macchiato",
        order=2,
        dark=True,
        colors=FlavorColors(
            rosewater=Color(
                name="Rosewater",
                identifier="rosewater",
                accent=True,
                order=0,
                hex="#f4dbd6",
                rgb=RGB(r=244, g=219, b=214),
                hsl=HSL(
                    h=9.999999999999963, s=0.5769230769230775, l=0.8980392156862745
                ),
            ),
            flamingo=Color(
                name="Flamingo",
                identifier="flamingo",
                accent=True,
                order=1,
                hex="#f0c6c6",
                rgb=RGB(r=240, g=198, b=198),
                hsl=HSL(h=0, s=0.5833333333333333, l=0.8588235294117648),
            ),
            pink=Color(
                name="Pink",
                identifier="pink",
                accent=True,
                order=2,
                hex="#f5bde6",
                rgb=RGB(r=245, g=189, b=230),
                hsl=HSL(
                    h=316.0714285714286, s=0.7368421052631583, l=0.8509803921568628
                ),
            ),
            mauve=Color(
                name="Mauve",
                identifier="mauve",
                accent=True,
                order=3,
                hex="#c6a0f6",
                rgb=RGB(r=198, g=160, b=246),
                hsl=HSL(
                    h=266.51162790697674, s=0.8269230769230772, l=0.7960784313725491
                ),
            ),
            red=Color(
                name="Red",
                identifier="red",
                accent=True,
                order=4,
                hex="#ed8796",
                rgb=RGB(r=237, g=135, b=150),
                hsl=HSL(
                    h=351.1764705882353, s=0.7391304347826088, l=0.7294117647058824
                ),
            ),
            maroon=Color(
                name="Maroon",
                identifier="maroon",
                accent=True,
                order=5,
                hex="#ee99a0",
                rgb=RGB(r=238, g=153, b=160),
                hsl=HSL(
                    h=355.05882352941177, s=0.7142857142857143, l=0.7666666666666666
                ),
            ),
            peach=Color(
                name="Peach",
                identifier="peach",
                accent=True,
                order=6,
                hex="#f5a97f",
                rgb=RGB(r=245, g=169, b=127),
                hsl=HSL(
                    h=21.355932203389827, s=0.8550724637681162, l=0.7294117647058824
                ),
            ),
            yellow=Color(
                name="Yellow",
                identifier="yellow",
                accent=True,
                order=7,
                hex="#eed49f",
                rgb=RGB(r=238, g=212, b=159),
                hsl=HSL(
                    h=40.253164556962034, s=0.6991150442477877, l=0.7784313725490196
                ),
            ),
            green=Color(
                name="Green",
                identifier="green",
                accent=True,
                order=8,
                hex="#a6da95",
                rgb=RGB(r=166, g=218, b=149),
                hsl=HSL(
                    h=105.21739130434783, s=0.4825174825174825, l=0.7196078431372549
                ),
            ),
            teal=Color(
                name="Teal",
                identifier="teal",
                accent=True,
                order=9,
                hex="#8bd5ca",
                rgb=RGB(r=139, g=213, b=202),
                hsl=HSL(
                    h=171.08108108108107, s=0.46835443037974706, l=0.6901960784313725
                ),
            ),
            sky=Color(
                name="Sky",
                identifier="sky",
                accent=True,
                order=10,
                hex="#91d7e3",
                rgb=RGB(r=145, g=215, b=227),
                hsl=HSL(
                    h=188.78048780487802, s=0.5942028985507245, l=0.7294117647058823
                ),
            ),
            sapphire=Color(
                name="Sapphire",
                identifier="sapphire",
                accent=True,
                order=11,
                hex="#7dc4e4",
                rgb=RGB(r=125, g=196, b=228),
                hsl=HSL(
                    h=198.64077669902912, s=0.6560509554140128, l=0.692156862745098
                ),
            ),
            blue=Color(
                name="Blue",
                identifier="blue",
                accent=True,
                order=12,
                hex="#8aadf4",
                rgb=RGB(r=138, g=173, b=244),
                hsl=HSL(h=220.188679245283, s=0.8281250000000003, l=0.7490196078431373),
            ),
            lavender=Color(
                name="Lavender",
                identifier="lavender",
                accent=True,
                order=13,
                hex="#b7bdf8",
                rgb=RGB(r=183, g=189, b=248),
                hsl=HSL(
                    h=234.46153846153848, s=0.8227848101265824, l=0.8450980392156863
                ),
            ),
            text=Color(
                name="Text",
                identifier="text",
                accent=False,
                order=14,
                hex="#cad3f5",
                rgb=RGB(r=202, g=211, b=245),
                hsl=HSL(
                    h=227.4418604651163, s=0.6825396825396831, l=0.8764705882352941
                ),
            ),
            subtext1=Color(
                name="Subtext 1",
                identifier="subtext1",
                accent=False,
                order=15,
                hex="#b8c0e0",
                rgb=RGB(r=184, g=192, b=224),
                hsl=HSL(h=228, s=0.39215686274509803, l=0.8),
            ),
            subtext0=Color(
                name="Subtext 0",
                identifier="subtext0",
                accent=False,
                order=16,
                hex="#a5adcb",
                rgb=RGB(r=165, g=173, b=203),
                hsl=HSL(
                    h=227.36842105263156, s=0.2676056338028167, l=0.7215686274509804
                ),
            ),
            overlay2=Color(
                name="Overlay 2",
                identifier="overlay2",
                accent=False,
                order=17,
                hex="#939ab7",
                rgb=RGB(r=147, g=154, b=183),
                hsl=HSL(
                    h=228.33333333333331, s=0.2000000000000001, l=0.6470588235294117
                ),
            ),
            overlay1=Color(
                name="Overlay 1",
                identifier="overlay1",
                accent=False,
                order=18,
                hex="#8087a2",
                rgb=RGB(r=128, g=135, b=162),
                hsl=HSL(
                    h=227.6470588235294, s=0.1545454545454545, l=0.5686274509803921
                ),
            ),
            overlay0=Color(
                name="Overlay 0",
                identifier="overlay0",
                accent=False,
                order=19,
                hex="#6e738d",
                rgb=RGB(r=110, g=115, b=141),
                hsl=HSL(
                    h=230.32258064516128, s=0.12350597609561753, l=0.49215686274509807
                ),
            ),
            surface2=Color(
                name="Surface 2",
                identifier="surface2",
                accent=False,
                order=20,
                hex="#5b6078",
                rgb=RGB(r=91, g=96, b=120),
                hsl=HSL(
                    h=229.65517241379308, s=0.13744075829383887, l=0.4137254901960784
                ),
            ),
            surface1=Color(
                name="Surface 1",
                identifier="surface1",
                accent=False,
                order=21,
                hex="#494d64",
                rgb=RGB(r=73, g=77, b=100),
                hsl=HSL(
                    h=231.11111111111114, s=0.15606936416184972, l=0.3392156862745098
                ),
            ),
            surface0=Color(
                name="Surface 0",
                identifier="surface0",
                accent=False,
                order=22,
                hex="#363a4f",
                rgb=RGB(r=54, g=58, b=79),
                hsl=HSL(h=230.4, s=0.1879699248120301, l=0.2607843137254902),
            ),
            base=Color(
                name="Base",
                identifier="base",
                accent=False,
                order=23,
                hex="#24273a",
                rgb=RGB(r=36, g=39, b=58),
                hsl=HSL(
                    h=231.8181818181818, s=0.23404255319148934, l=0.1843137254901961
                ),
            ),
            mantle=Color(
                name="Mantle",
                identifier="mantle",
                accent=False,
                order=24,
                hex="#1e2030",
                rgb=RGB(r=30, g=32, b=48),
                hsl=HSL(
                    h=233.33333333333334, s=0.23076923076923075, l=0.15294117647058825
                ),
            ),
            crust=Color(
                name="Crust",
                identifier="crust",
                accent=False,
                order=25,
                hex="#181926",
                rgb=RGB(r=24, g=25, b=38),
                hsl=HSL(
                    h=235.71428571428572, s=0.22580645161290322, l=0.12156862745098039
                ),
            ),
        ),
    ),
    mocha=Flavor(
        name="Mocha",
        identifier="mocha",
        order=3,
        dark=True,
        colors=FlavorColors(
            rosewater=Color(
                name="Rosewater",
                identifier="rosewater",
                accent=True,
                order=0,
                hex="#f5e0dc",
                rgb=RGB(r=245, g=224, b=220),
                hsl=HSL(h=9.599999999999968, s=0.555555555555556, l=0.911764705882353),
            ),
            flamingo=Color(
                name="Flamingo",
                identifier="flamingo",
                accent=True,
                order=1,
                hex="#f2cdcd",
                rgb=RGB(r=242, g=205, b=205),
                hsl=HSL(h=0, s=0.587301587301587, l=0.8764705882352941),
            ),
            pink=Color(
                name="Pink",
                identifier="pink",
                accent=True,
                order=2,
                hex="#f5c2e7",
                rgb=RGB(r=245, g=194, b=231),
                hsl=HSL(
                    h=316.4705882352941, s=0.7183098591549301, l=0.8607843137254902
                ),
            ),
            mauve=Color(
                name="Mauve",
                identifier="mauve",
                accent=True,
                order=3,
                hex="#cba6f7",
                rgb=RGB(r=203, g=166, b=247),
                hsl=HSL(
                    h=267.4074074074074, s=0.8350515463917528, l=0.8098039215686275
                ),
            ),
            red=Color(
                name="Red",
                identifier="red",
                accent=True,
                order=4,
                hex="#f38ba8",
                rgb=RGB(r=243, g=139, b=168),
                hsl=HSL(
                    h=343.2692307692308, s=0.8124999999999998, l=0.7490196078431373
                ),
            ),
            maroon=Color(
                name="Maroon",
                identifier="maroon",
                accent=True,
                order=5,
                hex="#eba0ac",
                rgb=RGB(r=235, g=160, b=172),
                hsl=HSL(h=350.4, s=0.6521739130434779, l=0.7745098039215685),
            ),
            peach=Color(
                name="Peach",
                identifier="peach",
                accent=True,
                order=6,
                hex="#fab387",
                rgb=RGB(r=250, g=179, b=135),
                hsl=HSL(h=22.95652173913043, s=0.92, l=0.7549019607843137),
            ),
            yellow=Color(
                name="Yellow",
                identifier="yellow",
                accent=True,
                order=7,
                hex="#f9e2af",
                rgb=RGB(r=249, g=226, b=175),
                hsl=HSL(
                    h=41.35135135135135, s=0.8604651162790699, l=0.8313725490196078
                ),
            ),
            green=Color(
                name="Green",
                identifier="green",
                accent=True,
                order=8,
                hex="#a6e3a1",
                rgb=RGB(r=166, g=227, b=161),
                hsl=HSL(
                    h=115.45454545454544, s=0.5409836065573769, l=0.7607843137254902
                ),
            ),
            teal=Color(
                name="Teal",
                identifier="teal",
                accent=True,
                order=9,
                hex="#94e2d5",
                rgb=RGB(r=148, g=226, b=213),
                hsl=HSL(
                    h=170.00000000000003, s=0.5735294117647057, l=0.7333333333333334
                ),
            ),
            sky=Color(
                name="Sky",
                identifier="sky",
                accent=True,
                order=10,
                hex="#89dceb",
                rgb=RGB(r=137, g=220, b=235),
                hsl=HSL(
                    h=189.18367346938774, s=0.7101449275362316, l=0.7294117647058823
                ),
            ),
            sapphire=Color(
                name="Sapphire",
                identifier="sapphire",
                accent=True,
                order=11,
                hex="#74c7ec",
                rgb=RGB(r=116, g=199, b=236),
                hsl=HSL(h=198.5, s=0.759493670886076, l=0.6901960784313725),
            ),
            blue=Color(
                name="Blue",
                identifier="blue",
                accent=True,
                order=12,
                hex="#89b4fa",
                rgb=RGB(r=137, g=180, b=250),
                hsl=HSL(
                    h=217.1681415929203, s=0.9186991869918699, l=0.7588235294117647
                ),
            ),
            lavender=Color(
                name="Lavender",
                identifier="lavender",
                accent=True,
                order=13,
                hex="#b4befe",
                rgb=RGB(r=180, g=190, b=254),
                hsl=HSL(
                    h=231.89189189189187, s=0.9736842105263159, l=0.8509803921568628
                ),
            ),
            text=Color(
                name="Text",
                identifier="text",
                accent=False,
                order=14,
                hex="#cdd6f4",
                rgb=RGB(r=205, g=214, b=244),
                hsl=HSL(
                    h=226.15384615384616, s=0.6393442622950825, l=0.8803921568627451
                ),
            ),
            subtext1=Color(
                name="Subtext 1",
                identifier="subtext1",
                accent=False,
                order=15,
                hex="#bac2de",
                rgb=RGB(r=186, g=194, b=222),
                hsl=HSL(h=226.66666666666669, s=0.35294117647058837, l=0.8),
            ),
            subtext0=Color(
                name="Subtext 0",
                identifier="subtext0",
                accent=False,
                order=16,
                hex="#a6adc8",
                rgb=RGB(r=166, g=173, b=200),
                hsl=HSL(
                    h=227.6470588235294, s=0.23611111111111102, l=0.7176470588235294
                ),
            ),
            overlay2=Color(
                name="Overlay 2",
                identifier="overlay2",
                accent=False,
                order=17,
                hex="#9399b2",
                rgb=RGB(r=147, g=153, b=178),
                hsl=HSL(
                    h=228.38709677419354, s=0.16756756756756758, l=0.6372549019607843
                ),
            ),
            overlay1=Color(
                name="Overlay 1",
                identifier="overlay1",
                accent=False,
                order=18,
                hex="#7f849c",
                rgb=RGB(r=127, g=132, b=156),
                hsl=HSL(
                    h=229.65517241379308, s=0.12775330396475776, l=0.5549019607843138
                ),
            ),
            overlay0=Color(
                name="Overlay 0",
                identifier="overlay0",
                accent=False,
                order=19,
                hex="#6c7086",
                rgb=RGB(r=108, g=112, b=134),
                hsl=HSL(
                    h=230.7692307692308, s=0.10743801652892565, l=0.4745098039215686
                ),
            ),
            surface2=Color(
                name="Surface 2",
                identifier="surface2",
                accent=False,
                order=20,
                hex="#585b70",
                rgb=RGB(r=88, g=91, b=112),
                hsl=HSL(h=232.5, s=0.12, l=0.39215686274509803),
            ),
            surface1=Color(
                name="Surface 1",
                identifier="surface1",
                accent=False,
                order=21,
                hex="#45475a",
                rgb=RGB(r=69, g=71, b=90),
                hsl=HSL(
                    h=234.2857142857143, s=0.13207547169811326, l=0.31176470588235294
                ),
            ),
            surface0=Color(
                name="Surface 0",
                identifier="surface0",
                accent=False,
                order=22,
                hex="#313244",
                rgb=RGB(r=49, g=50, b=68),
                hsl=HSL(
                    h=236.84210526315792, s=0.16239316239316234, l=0.22941176470588237
                ),
            ),
            base=Color(
                name="Base",
                identifier="base",
                accent=False,
                order=23,
                hex="#1e1e2e",
                rgb=RGB(r=30, g=30, b=46),
                hsl=HSL(h=240, s=0.21052631578947367, l=0.14901960784313725),
            ),
            mantle=Color(
                name="Mantle",
                identifier="mantle",
                accent=False,
                order=24,
                hex="#181825",
                rgb=RGB(r=24, g=24, b=37),
                hsl=HSL(h=240, s=0.2131147540983607, l=0.11960784313725491),
            ),
            crust=Color(
                name="Crust",
                identifier="crust",
                accent=False,
                order=25,
                hex="#11111b",
                rgb=RGB(r=17, g=17, b=27),
                hsl=HSL(h=240, s=0.22727272727272727, l=0.08627450980392157),
            ),
        ),
    ),
)
