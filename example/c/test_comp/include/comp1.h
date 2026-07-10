/**
 * @file comp1.h
 * @brief This is a test file for comp1
 *
 * To use this driver:
 * - include this file in your project
 * - @ref print() is a function that prints "Hello World!"
 */

/**
 * @brief print function
 *
 */
void print(void);

/**
 * @brief print the added result
 *
 * @param a aaa
 * @param b bbb
 */
void add(comp1 a, comp1 b);


/**
 * @brief THIS IS TEST_FOO VARIABLE!
 *
 */
#define TEST_FOO 111;


/**
 * @brief struct comp
 *
 */
struct comp1
{
    /**
     * @brief ??? foo?
     *
     */
    int foo;
    int bar;
};


/**
 * @brief BSP display configuration structure
 *
 */
typedef struct {
    lvgl_port_cfg_t lvgl_port_cfg;  /*!< LVGL port configuration */
    uint32_t        buffer_size;    /*!< Size of the buffer for the screen in pixels */
    bool            double_buffer;  /*!< True, if should be allocated two buffers */
    struct {
        unsigned int buff_dma: 1;    /*!< Allocated LVGL buffer will be DMA capable */
        unsigned int buff_spiram: 1; /*!< Allocated LVGL buffer will be in PSRAM */
    } flags;
} bsp_display_cfg_t;


/**
 * @brief typedef int for comp
 *
 */
typedef int comp1_int;


/**
 * @brief it's a union!!!
 *
 */
union union_comp1
{
    comp1 a;
    comp1 b;
};


/**
 * @brief Struct with a fully anonymous union member (no instance name).
 *
 */
typedef struct {
    int kind;             /*!< discriminator for the union below */
    union {
        int int_value;    /*!< value when kind is an integer */
        float float_value; /*!< value when kind is a float */
    };
} anonymous_union_comp1_t;
