from lcfp_cli import parse_args, get_output_format, get_xaxis_units, get_yaxis_units
from light_curve_constructor import light_curve_generator

def main():
    args = parse_args()
    output_settings = get_output_format(args.output_type)
    x_settings = get_xaxis_units(args.xaxis)
    y_settings = get_yaxis_units(args.yaxis, args.flux_units)

    light_curve_generator(data=args.input_file,
                          flux_units=args.flux_units,
                          time_sel=x_settings,
                          brightness_sel=y_settings,
                          scale_sel=args.scale,
                          output_sel=output_settings,
                          xmin=args.xmin,
                          xmax=args.xmax,
                          ymin=args.ymin,
                          ymax=args.ymax)
    
if __name__ == '__main__':
    main()