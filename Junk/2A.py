        MATCH(
            'argument_2A_match',
            (
                  (
                        name_1
                      + OPTIONAL(dot + name_2)
                      + OPTIONAL(
                              GROUP('left_parenthesis', ow + '(')                                        #   )
                            + ow
                        )
                  )

                  (name | number | single_quote)
                + GROUP('operator__ow', ow + GROUP('operator', ANY_OF('(', ')', ',')) + middle_ow)
            )
        )

